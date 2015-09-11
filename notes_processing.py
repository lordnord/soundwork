from soundwork.notes import *
from soundwork.wavefile import open
from soundwork import waveforms

new = open('new-notes.wav', 'w')
new.set(8, 44100)

ladder = 'C0 C#0 D0 D#0 E0 F0 F#0 G0 G#0 A0 A#0 B0'

for i in range(7):
    for note, length in parser('1/4 ' + ladder, bpm=70):
        note.up(OCTAVE * i)
        new.gen(waveforms.square(note.freq), length)
        
new.close()
