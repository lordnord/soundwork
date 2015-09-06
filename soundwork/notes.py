from __future__ import division

# Note frequencies for 10th octave
NOTES = {
'C'  : 16744.036,
'C#' : 17739.688,
'D'  : 18794.545,
'D#' : 19912.127,
'E'  : 21096.164,
'F'  : 22350.607,
'F#' : 23679.643,
'G'  : 25087.708,
'G#' : 26579.501,
'A'  : 28160.000,
'A#' : 29834.481,
'B'  : 31608.531,
}

def single(note):
    'Generates frequency by note sign and octave'
    if isinstance(note, str):
        sign, octave = note.split('.')
        octave = int(octave)
    else:
        sign, octave = note
    return NOTES[sign] / (2 ** (10-octave))


def muslength(le, bpm=None):
    # Returns note length in ms for BPM
    if bpm == None:
        bpm = muslength.last
    measure = 60000.0 / bpm
    return measure * le

muslength.last = 70

def parser(melody):
    melody = melody.strip().replace('\n', ' ').split(' ')
    for note in melody:
        if 'P' in note:
            len = note.split('.')[0]
            freq = 0
        else:
            len, sign, octave = note.split('.')
            freq = NOTES[sign] / (2 ** (10-int(octave)))
        #yield (freq, int(muslength(eval(len))))
        yield (freq, int(len))

def sequencelength(seq, bpm=None):
    # BPM is temporary not used.
    return sum(x[1] for x in parser(seq))

