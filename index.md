A synthesizer that accepts voice commands to play sound and control the synth's parameters.
<br><br>

----
## Introduction
<br>
<div style="display:flex">
     <div style="flex:1;padding-right:10px;">
          <img src="images/speech_rec_pic.png" width="400" height="400"/>
     </div>
     <div style="flex:1;padding:10px;">
          <img src="images/synth_pic.jpeg" width="500" height="200"/>
     </div>
</div>

 
<br>
This project explores a new way of making music by using voice commands. So, instead of turning the knobs or moving the faders up and down, you can issue a voice command and the computer can do it for you. This add-on feature could benefit those who have weakness in hands that won't allow them to use the physical synth for a long time.
<br><br>

----
## Methods
Speech recognition and synthesizer are the two main topics covered in this project.
For the speech recognition sofware, I explored both Python online and offline engines. Primarily, [Google Speech Recognition](https://pypi.org/project/SpeechRecognition/) (online) and [VOSK API](https://alphacephei.com/vosk/) (offline). There's a significant delay in recognizing your voice in the Google Speech recognition engine, thus I ended up using VOSK API, which was faster and more reliable. For the synthesizer software, I used a platform called [SuperCollider](https://supercollider.github.io/), where I got all the sounds and music from by establishing OSC communication between Python and SuperCollider.

Singal flow block diagram:
<br><br>
<img src="images/blockdiagram.png"/>
<br><br>
Python and SC script:
<br><br>
<img src="images/app_ss.png" width="600" height="350"/>
<br><br>

----
## Demonstration video
video...
<br>

----
## Installation
If you're interested in trying out the prototype, please navigate to my [GitHub repository](https://github.com/tnguyen30/Voice-controlled-Synthesizer) for further instructions.
<br><br>

----
## Conclusion and further actions
This project is still at its early stage. There are various things needed to be fixed and changed for the synthesizer to achieve its stable form. Right now, its actions are quite straightforward, therefore, some other actions that I hope it can do include:

- Detect voice command during the playback
- Ability to record and save both the built-in sounds and from the input mic
- Apply audio effects on the input mic audio files as command
- Extend the audio effect library such as modulation, dynamic, and EQ
<br><br>

----
## References
Speech recognition image by Smashing Stocks: [Link](https://iconscout.com/icon/speech-recognition-2548780)
<br>
Synthesizer image by TONAL AXiS: [Link](https://tonalaxis.wordpress.com/2017/01/03/synth-art/)
<br>
Block diagram by Tien Nguyen
<br>
Python script is based on VOSK API developers' code [here](https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py)
<br>
SuperCollider script is based on SCAMP developers' code [here](https://www.youtube.com/watch?v=K2jZOdWegL8&ab_channel=MarcEvanstein%2Fmusic%E2%80%A4py)
