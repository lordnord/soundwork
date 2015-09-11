from soundwork.notes import *
from soundwork.wavefile import open
from soundwork.waveforms import *

new = open('new-notes.wav', 'w')
new.set(8, 44100)

ladder = 'C0 C#0 D0 D#0 E0 F0 F#0 G0 G#0 A0 A#0 B0'
melody = Sequence('1/4 ' + ladder)
instr = [sine, 1], [square, 4]

for i in range(7):
    melody.up(OCTAVE)
    new.fromnotes(melody, instr, bpm=70)
        
new.close()
