import wave
import random
import math

mono = wave.open('8mono.wav', 'r')
changed = wave.open('new.wav', 'w')

changed.setparams(mono.getparams())

def process(sample, pos):
    """
    Do something with sample as an integers in range 0-255
    """
    if sample == 0:
        res = 0
    else:
    
        res = sample * 2
        
    if res > 127:
        res = 127
    elif res < -128:
        res = -128
    return res

print 'End point is', mono.getnframes()

for i in range(mono.getnframes()):
    # print '\r', i,
    sample = mono.readframes(1)
    out = process(ord(sample) - 128, i) + 128
    changed.writeframes(chr(int(out)))
    
mono.close()
changed.close()