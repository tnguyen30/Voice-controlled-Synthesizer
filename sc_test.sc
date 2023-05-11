// Obtain your SC port
NetAddr.langPort

// You can test to make sure the OSC message is received here
OSCFunc.trace(hideStatusMsg: true)


// Might have to free the synth if experiencing delays or it doesn't sound correct

// String instrument (original code is by thor https://sc-users.bham.ac.narkive.com/0KTaBrrL/guitar-synthdef)
(
ScampUtils.instrumentFromSynthDef(
	SynthDef("string", {arg out=0, freq=440, pan=0, sustain=0.5, volume=0.3, gate=0, delaytime=0.1;
var pluck, period, string;
pluck = PinkNoise.ar(Decay.kr(Impulse.kr(0.005), 0.05));
period = freq.reciprocal;
string = CombL.ar(pluck, period, period, sustain*6);
string = LeakDC.ar(LPF.ar(Pan2.ar(string, pan), 12000)) * volume;
DetectSilence.ar(string, doneAction: 2);
Out.ar(out, string)
}))
)

(
ScampUtils.instrumentFromSynthDef(
	SynthDef("delaystring", {arg out=0, freq=440, pan=0, sustain=0.5, volume=0.3, delaytime=0.2, gate=0;
var pluck, period, string, effect;
pluck = PinkNoise.ar(Decay.kr(Impulse.kr(0.005), 0.05));
period = freq.reciprocal;
string = CombL.ar(pluck, period, period, sustain*6);
string = LeakDC.ar(LPF.ar(Pan2.ar(string, pan), 12000)) * volume;
effect = DelayN.ar(string, 0.2, delaytime, 1, string);
DetectSilence.ar(effect, doneAction:2);
Out.ar(out, effect)
}))
)

// A synth by Marc Evanstein: https://www.youtube.com/watch?v=K2jZOdWegL8&ab_channel=MarcEvanstein%2Fmusic%E2%80%A4py
(
ScampUtils.instrumentFromSynthDef(
	SynthDef("cloud", {
	arg panCenter=0, panWidth=0.3, freq=640, freqVariation=0.1, volume=0.7, gate=0;
	var grainPan = WhiteNoise.ar(panWidth, panCenter);
	var grainFreq = WhiteNoise.ar(freqVariation * freq, freq);
	var grainTrigger = Impulse.kr(20);
	var granulator = GrainSin.ar(2, grainTrigger, 0.06, grainFreq, grainPan);
	var env = EnvGate(gate:gate, fadeTime:0.1, doneAction: 2);
	Out.ar(0,granulator * volume * env);
}))
)