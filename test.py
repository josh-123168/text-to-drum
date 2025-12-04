from playsound3 import playsound
import threading
import time

bpm = 120
delay = 1 # 60/bpm

kick = "audio/kick.wav"
snare = "audio/snare.wav"
hat = "audio/hat.wav"
darren = "audio/darren.mp3"
rest = "audio/empty.mp3"

# start = time.perf_counter()

# playsound(kick, block=False)
# while time.perf_counter() - start < delay:
#     pass
# playsound(snare)

def wait():
    end_time = time.perf_counter() + delay
    while time.perf_counter() < end_time:
        pass

print("3")
wait()
print("2")
wait()
print("1")