from soundwork.notes import *
from soundwork.wavefile import open
from soundwork.waveforms import *

new = open('new-notes.wav', 'w')
new.set(8, 44100)

classic = """1/8 E6 D#6 E6 D#6 E6 B5 D6 C6 3/8 A5 1/8 _ E5 A5
3/8 B5 1/8 E5 G#5 B5 3/8 C6"""
x = Sequence(classic)
print x
x.reverse()
print x

ladder = 'C0 C#0 D0 D#0 E0 F0 F#0 G0 G#0 A0 A#0 B0'
melody = Sequence('1/4 ' + ladder)
instr = [sine, 1], [square, 4]

for i in range(7):
    melody.up(OCTAVE)
    print melody
    #new.fromnotes(melody, instr, bpm=70)
        
new.close()
