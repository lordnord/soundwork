import wave
import struct
import random
import math

self = wave.open('new.wav', 'w')
LEN = 44100
PARAMS = (1, 1, 44100, LEN, 'NONE', 'not compressed')
self.setparams(PARAMS)

qrate = self.getframerate() / 360.0

def getwavelength(freq):
    """
    Returns wave length in samples for freq.
    """
    res = self.getframerate() / freq
    return res

def amplit(percent):
    full = 2 ** (8 ** self.getsampwidth()) / 2 - 1
    out = percent * full /100.0
    return int(out)
    
def sine(pos, freq=50, amp=127):
    """
    Generates a sine wave with frequency = 50 and amplitude = 127.
    """
    
    res = math.sin(math.radians(pos * freq) / qrate) * amp
    
    if res > 127:
        res = 127
    elif res < -128:
        res = -128
    return int(res)
process = sine

print 'End point is', LEN

for i in range(LEN):
    # print '\r', i,
    x = sine(i) + 128
    self.writeframes(struct.pack('B', x))
    
self.close()
