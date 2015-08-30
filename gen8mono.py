import wave
import random
import math

self = wave.open('new.wav', 'w')
LEN = 44100
PARAMS = (1, 2, 44100, LEN, 'NONE', 'not compressed')
self.setparams(PARAMS)

qrate = self.getframerate() / 360.0


def amplit(percent):
    full = 2 ** (8 ** self.getsampwidth()) / 2 - 1
    out = percent * full /100.0
    return int(out)
    
def process(pos):
    """
    Do something with sample as an integers in range 0-255
    """
    # if sample == 0:
    #     res = 0
    # else:
        # res = sample * 2
    
    # Generates a sine wave with frequency = 50 and amplitude = 127.
    freq = 50
    amp = 127
    res = math.sin(math.radians(pos * freq) / qrate) * amp
    
        
    if res > 127:
        res = 127
    elif res < -128:
        res = -128
    return int(res)

print 'End point is', LEN

for i in range(LEN):
    # print '\r', i,
    x = process(i) + 128
    self.writeframes(chr(x))
    
self.close()