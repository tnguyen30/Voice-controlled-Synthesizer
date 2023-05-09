# Voice-controlled Synthesizer
A synthesizer that accepts voice commands to play sound and control the synth's parameters.
<br>
----
## About the project
This project explores a new way of making music by using voice commands. So, instead of turning the knobs or moving the faders up and down, you can issue a voice command and the computer can do it for you. This add-on feature could benefit those who have weakness in hands that won’t allow them to use the physical synth for a long time.
<br>
Check out the webpage for more details. [Link](https://tnguyen30.github.io/Voice-controlled-Synthesizer/)
<br>
----
## Installation
To run the test script, you will need to instal VOSK API (instructions are [here](https://alphacephei.com/vosk/install)) and you need to download the US English language model as well ([models](https://alphacephei.com/vosk/models)), and then download the SuperCollider software ([here](https://supercollider.github.io/downloads)).
<br>
In addition to the speech recognition package, I used another Python library called SCAMP (Suite for Computer-Assisted Music in Python) to establish the OSC communication. Here are its [documentation](http://scamp.marcevanstein.com/) and [installation](https://pypi.org/project/scamp/). I also include the tutorial [link](https://www.youtube.com/watch?v=K2jZOdWegL8&ab_channel=MarcEvanstein%2Fmusic%E2%80%A4py) made by Marc Evanstein on how to get SCAMP on SuperCollider. Alternatively, you can just establish a simpler [OSC communication](https://doc.sccode.org/Guides/OSC_communication.html) and that would require you to modify the scripts.
<br>
Finally, you can dowload the ().py and ().sc in this repository to your computer. Make sure to open the SuperCollider file while running the Python file and modify both scripts as needed.
<br>

----
## References
Python script is based on VOSK API developers' code [here](https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py)
<br>
SuperCollider script is based on SCAMP developers' code [here](https://www.youtube.com/watch?v=K2jZOdWegL8&ab_channel=MarcEvanstein%2Fmusic%E2%80%A4py)


