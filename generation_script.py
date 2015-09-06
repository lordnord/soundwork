from soundwork import wavefile, waveforms, notes

#melody = "1/4 C#4 P C#4 P C4 P P B3 P E4 P A3 P C4 C4 P "

melody = """100.C#.4 100.P 100.C#.4 100.P 100.C.4
200.P 100.B.3 100.P 100.E.4 100.P 100.A.3 100.P 200.C.4 100.P """

new = wavefile.open('buildy.wav', 'w')
new.set(8, 44100, notes.sequencelength(melody))

for freq, leng in notes.parser(melody):
    new.gen(waveforms.sine(freq), leng)
    
new.close()