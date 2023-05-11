# Prerequisites: 
# Download python module `sounddevice` by simply run command `pip install sounddevice`
# Change path of the en-us language model to where you store it on your computer
# Make sure you have already installed vosk and scamp library
# Make sure to open SC before running the script

import argparse
import threading
import queue
import sys
import sounddevice as sd
import json

from scamp import *
import random

from vosk import Model, KaldiRecognizer

# queue from vosk
q = queue.Queue()

# open a scamp session
s = Session()

# for vosk 
def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    "-l", "--list-devices", action="store_true",
    help="show list of audio devices and exit")
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    "-f", "--filename", type=str, metavar="FILENAME",
    help="audio file to store recording to")
parser.add_argument(
    "-d", "--device", type=int_or_str,
    help="input device (numeric ID or substring)")
parser.add_argument(
    "-r", "--samplerate", type=int, help="sampling rate")
parser.add_argument(
    "-m", "--model", type=str, help="language model; e.g. en-us, fr, nl; default is en-us")
args = parser.parse_args(remaining)

try:
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, "input")
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info["default_samplerate"])
    
    # change the path to where you store your model package
    if args.model is None:
        model = Model("/Users/itstien/Desktop/voice_assistant_pypcktest/vosk-model-small-en-us-0.15")
    else:
        model = Model("/Users/itstien/Desktop/voice_assistant_pypcktest/vosk-model-small-en-us-0.15")

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    # getting live data stream
    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype="int16", channels=1, callback=callback):
        print("#" * 80)
        print("Press Ctrl+C to stop the recording")
        print("#" * 80)

        rec = KaldiRecognizer(model, args.samplerate)

        # initialize the synthdefs and open SC port
        to_sc = s.new_osc_part("cloud", port=57120)
        to_sc2 = s.new_osc_part("string", port=57120)
        to_sc3 = s.new_osc_part("delaystring", port=57120)

        # speech recognition loop
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                recognizerResult = rec.Result()
                # convert the recognizerResult string into a dictionary  
                resultDict = json.loads(recognizerResult)

                # assigning the commands to the different instruments

                # Run "cloud" synthdef in SC
                if resultDict.get("text", "") == "hello":
                    # print to indicate command received
                    print("here")
                    # play the pitches from SC
                    for pitch in [74,72]:
                        to_sc.play_note(pitch,[0.7,0],0.5)

                # synth random melody
                if resultDict.get("text", "") == "synthesizer":
                    print("here")
                    for pitch in [70,40,53,72,60,52]:
                        to_sc.play_note(pitch,[0.7,0],2, "param_freqVariation: [0.01,0.5]",blocking=False)
                        wait(random.uniform(0.25,2))

                
                # Run "string" synthdef in SC
                # play the 5th interval
                if resultDict.get("text", "") == "play the fifth":
                    print("here")
                    for pitch in [60,67]:
                        to_sc2.play_note(pitch, [0.7,0], 0.5)

                    
                # play the 5th interval but volume is turned down
                if resultDict.get("text", "") == "volume down":
                    print("here")
                    for pitch in [60,67]:
                        to_sc2.play_note(pitch, [0.3,0], 0.5)
                        
                # string scale
                if resultDict.get("text", "") == "play scale":
                    print("here")
                    for pitch in [60,62,64,65,67,69,71,72]:
                        to_sc2.play_note(pitch, [0.7,0], 0.5)


                # Run "stringdelay" synthdef in SC
                # string the 5th delay
                if resultDict.get("text", "") == "delay effect":
                    print("here")
                    for pitch in [60,67,72]:
                        to_sc3.play_note(pitch, [0.7,0], 0.5)

                    
                # quit the program
                if resultDict.get("text", "") == "goodbye":
                    print("\nDone")
                    parser.exit(0)
               
            else:
                print(rec.PartialResult())
            if dump_fn is not None:
                dump_fn.write(data)

            
except KeyboardInterrupt:
    print("\nDone")
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ": " + str(e))