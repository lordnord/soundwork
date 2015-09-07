from __future__ import division
from fractions import Fraction

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

class NotationError(Exception):
    pass

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

def msec_parser(melody):
    melody = melody.strip().replace('\n', ' ').split(' ')
    for note in melody:
        if 'P' in note:
            len = note.split('.')[0]
            freq = 0
        else:
            len, sign, octave = note.split('.')
            freq = NOTES[sign] / (2 ** (10-int(octave)))
        yield (freq, int(len))

def bpm_parser(melody, bpm):
    melody = melody.strip().replace('\n', ' ').split(' ')
    if '/' not in melody[0]:
        raise NotationError("Notes length isn't specified.")
        
    for record in melody:
        if '/' in record:
            note_len = Fraction(record) * 60000 / bpm
            continue
            
        if record in ('_', 'P'):
            freq = 0
        else:
            sign, octave = record[:-1], record[-1]
            freq = NOTES[sign] / (2 ** (10-int(octave)))
            
        yield (freq, int(note_len))
    
def parser(melody, bpm=None):
    if bpm:
        return bpm_parser(melody, bpm)
    else:
        return msec_parser(melody)

def sequencelength(seq, bpm=None):
    return sum(x[1] for x in parser(seq, bpm))

