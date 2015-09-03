from soundwork import wavefile, waveforms, notes

melody = """1/4.C#.4 1/4.P 1/4.C#.4 1/4.P 1/4.C.4
1/2.P 1/4.B.3 1/4.P 1/4.E.4 1/4.P 1/4.A.3 1/4.P 1/2.C.4 1/4.P """

new = wavefile.open('buildy.wav', 'w')
lenght = notes.seqencelenght(melody * 4)
new.set(8, 44100, lenght)

for freq, length in notes.parser(melody*4):
    new.gen(waveforms.sine(freq), length)
    
new.gen(waveforms.zfill)
new.close()