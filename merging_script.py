from soundwork import wavefile
from soundwork.waveforms import *

melody = """1/8 E6 D#6 E6 D#6 E6 B5 D6 C6 3/8 A5 1/8 _ E5 A5
3/8 B5 1/8 E5 G#5 B5 3/8 C6"""

new = wavefile.open('build-merg.wav', 'w')
new.set(8, 44100)

zigzag = [sine, 1], [square, 4]
new.fromnotes(melody, zigzag, bpm=50)
new.fromnotes(melody, [sine, 1], bpm=70)
new.fromnotes(melody, zigzag, bpm=60)
new.fromnotes(melody, [sine, 1], bpm=80)

new.close()