import random
import math
import wavefile

def sine(freq):
    def wrapped(file, pos):
        w = (2 * math.pi * freq) / file.getframerate()
        res = math.sin(pos * w) * file.amplit(100)
        return int(res)
    return wrapped
    


BPM = 70
sequence = """
1/8 E6 D#6 E6 D#6 E6 B5 D6 C6 3/8 A5 1/8 P 
E5 A5 3/8 B5 1/8 E5 G#5 B5 3/8 C6
"""


new = wavefile.open('build2.wav', 'w')
# lenght = new.len(sequence)
lenght = 1000
new.set(8, 44100, lenght)
new.gen(sine(freq=220))
del new