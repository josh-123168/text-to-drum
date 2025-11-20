from playsound3 import playsound
import time
import threading

bpm = 240
delay = 60/bpm

f = False
t = True

def kick(b):
    playsound("audio/kick.wav", block=b)
    threading.Event().wait(delay)

def snare(b):
    playsound("audio/snare.wav", block=b)
    threading.Event().wait(delay)

def hat(b):
    playsound("audio/hat.wav", block=b)
    threading.Event().wait(delay)

kick(f)
hat(f)
snare(f)
hat(f)
hat(f)
kick(f)
snare(f)
hat(f)
kick(f)
hat(f)
snare(f)
hat(f)
hat(f)
kick(f)
snare(f)
hat(f)
kick(f)
hat(f)
snare(f)
hat(f)
hat(f)
kick(f)
snare(f)
hat(t)