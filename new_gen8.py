import random
import math

import wavefile


def proc(file, pos):
    """Generates a sine wave with frequency = 50 and amplitude = 127"""
    freq = 50
    amp = 127
    qrate = file.getframerate() / 360.0
    res = math.sin(math.radians(pos * freq) / qrate) * amp
            
    if res > 127:
        res = 127
    elif res < -128:
        res = -128
    return int(res)

new = wavefile.open('build1.wav', 'w')
new.set(8, 44100, 1000)
new.gen(proc)
del new