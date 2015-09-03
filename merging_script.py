from soundwork import wavefile, notes
from soundwork.waveforms import sine, merge

melody = """100.C#.4 100.P 100.C#.4 100.P 100.C.4
200.P 100.B.3 100.P 100.E.4 100.P 100.A.3 100.P 200.C.4 100.P """

new = wavefile.open('buildy.wav', 'w')
lenght = notes.sequencelenght(melody * 4)
new.set(8, 44100, 10000)

def merging():
    print 'm'
    for freq, length in notes.parser(melody):
        merged = merge(sine(freq), sine(freq/4))
        new.gen(merged, length)
    
def simple():
    print 's'
    for freq, length in notes.parser(melody):
        new.gen(sine(freq), length)
    
merging()
simple()
merging()
simple()
new.gen(waveforms.zfill)
new.close()