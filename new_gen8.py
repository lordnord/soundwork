import random
import math
import wavefile

def proc(file, pos):
    """Generates a sine wave with frequency = 50 and amplitude = 127"""
    freq = 6050
    qrate = file.getframerate() / 360.0
    res = math.sin(pos * freq) * file.amplit(100)
    return int(res)


BPM = 70
sequence = """
1/8 E6 D#6 E6 D#6 E6 B5 D6 C6 3/8 A5 1/8 P 
E5 A5 3/8 B5 1/8 E5 G#5 B5 3/8 C6
"""


new = wavefile.open('build2.wav', 'w')
# lenght = new.len(sequence)
lenght = 1000
new.set(8, 44100, lenght)
new.gen(sequence)
del new