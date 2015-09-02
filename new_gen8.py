import random
import math

import wavefile


def proc(file, pos):
    """Generates a sine wave with frequency = 50 and amplitude = 127"""
    freq = 6050
    qrate = file.getframerate() / 360.0
    res = math.sin(pos * freq) * file.amplit(100)

    return int(res)

new = wavefile.open('build2.wav', 'w')
new.set(8, 44100, 1000)
new.gen(proc)
del new