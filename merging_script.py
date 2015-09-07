from soundwork import wavefile, notes
from soundwork.waveforms import sine, square, merge

#melody = """100.C#.4 100.P 100.C#.4 100.P 100.C.4
#200.P 100.B.3 100.P 100.E.4 100.P 100.A.3 100.P 200.C.4 100.P """

melody = """1/8 E6 D#6 E6 D#6 E6 B5 D6 C6 3/8 A5 1/8 _ E5 A5
3/8 B5 1/8 E5 G#5 B5 3/8 C6 _"""

new = wavefile.open('build-merg.wav', 'w')
new.set(8, 44100)

def merging():
    for freq, length in notes.parser(melody, bpm=50):
        merged = merge(sine(freq), square(freq*4))
        new.gen(merged, length)
    
def simple():
    for freq, length in notes.parser(melody, bpm=50):
        new.gen(sine(freq), length)
    
merging()
simple()
merging()
simple()
new.close()