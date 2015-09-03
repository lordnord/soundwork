import wave
import struct

import random
import math

mono = wave.open('16mono.wav', 'r')
changed = wave.open('new2.wav', 'w')

changed.setparams(mono.getparams())

def process(sample, pos):
    """
    Do something with sample as an integer in range 0-65535
    """
    #return random.randrange(65536)
    if sample > 20000: return 20000
    return sample

print 'End point is', mono.getnframes()

for pos in range(mono.getnframes()):
    print '\r', pos,
    sample = mono.readframes(1)
    intsample = struct.unpack('<H', sample)[0]
    out = process(intsample - 32768, pos) + 32768
    tochanged = struct.pack('<H', out)
    changed.writeframes(tochanged)
    
mono.close()
changed.close()