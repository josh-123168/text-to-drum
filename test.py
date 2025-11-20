from playsound3 import playsound
import threading
import time

bpm = 120
delay = 60/bpm

kick = "audio/kick.wav"
snare = "audio/snare.wav"
hat = "audio/hat.wav"
darren = "audio/darren.mp3"
rest = "audio/empty.mp3"

start = time.perf_counter()

playsound(kick, block=False)
while time.perf_counter() - start < delay:
    pass
playsound(snare)