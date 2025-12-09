from playsound3 import playsound
import threading
import sys

bpm = int(input("Enter BPM (60-240):"))
if bpm < 60 or bpm > 240:
    print("BPM error")
    sys.exit()

delay = 30/bpm

print("Kick:    '.'\n\n\nHi-Hat:  '-'\n\n\nSnare:   '='\n\n\nRest:    ' '\n")
beatstring = input("Enter eighth-note beat string (Min 2 characters):")

def translate(beat):
    beatlist = []
    val = 0
    for symbol in beat:
        if symbol == " ":
            val = 0
        elif symbol == ".":
            val = 1
        elif symbol == "-":
            val = 2
        elif symbol == "=":
            val = 3
        else:
            return
        beatlist.append(val)
    return beatlist

def wait():
    threading.Event().wait(delay)
   
def kick(b):
    playsound("audio/kick.wav", block=b)
    wait()

def snare(b):
    playsound("audio/snare.wav", block=b)
    wait()

def hat(b):
    playsound("audio/hat.wav", block=b)
    wait()

def rest(b):
    playsound("audio/empty.mp3", block=b)
    wait()

def playBeat(list):
    last = len(list) - 1
    duration = len(list) * delay
    finalsound = list.pop(last)
    for sound in list:
        if sound == 0:
            rest(False)
        elif sound == 1:
            kick(False)
        elif sound == 2:
            hat(False)
        elif sound == 3:
            snare(False)
    if finalsound == 0:
        rest(True)
    elif finalsound == 1:
        kick(True)
    elif finalsound == 2:
        hat(True)
    elif finalsound == 3:
        snare(True)
    print(f'Done (Beat Length: {duration:.2f}s)')

if len(beatstring) < 2:
    print("String too short")
elif translate(beatstring) == None:
    print("Unknown symbols")
else:
    print("Playing...")
    playBeat(translate(beatstring))