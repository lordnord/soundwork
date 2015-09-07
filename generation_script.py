from soundwork import wavefile, waveforms, notes

melody2 = "1/4 C#4 _ C#4 _ C4 _ _ B3 _ E4 _ A3 _ C4 C4 _ "

msec_notation = """100.C#.4 100.P 100.C#.4 100.P 100.C.4
200.P 100.B.3 100.P 100.E.4 100.P 100.A.3 100.P 200.C.4 100.P """

new = wavefile.open('buildy.wav', 'w')
new.set(8, 44100)

for freq, leng in notes.parser(melody2, bpm=130):
    new.gen(waveforms.square(freq), leng)
    
new.close()