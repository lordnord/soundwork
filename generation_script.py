from soundwork import wavefile, waveforms, notes

melody = """100.C#.4 100.P 100.C#.4 100.P 100.C.4
200.P 100.B.3 100.P 100.E.4 100.P 100.A.3 100.P 200.C.4 100.P """

new = wavefile.open('buildy.wav', 'w')
lenght = notes.seqencelenght(melody * 4)
new.set(8, 44100, lenght)

for freq, length in notes.parser(melody*4):
    new.gen(waveforms.sine(freq), length)
    
new.gen(waveforms.zfill)
new.close()