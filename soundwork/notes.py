from __future__ import division
from fractions import Fraction

PAUSE = '_'
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
PAUSE: 0,
}

class NotationError(Exception):
    pass

class Note:
    def __init__(self, note):
        if isinstance(note, str):
            if note == PAUSE:
                self.sign = PAUSE
                self.octave = None
            else:
                self.sign, self.octave = note[:-1], int(note[-1])
        else:
            self.sign, self.octave = note
        self._updatefreq()
        
    def _updatefreq(self):
        if self.sign == PAUSE:
            self.freq = 0
        else:
            self.freq = NOTES[self.sign] / (2 ** (10-self.octave))
        
    def __str__(self):
        if self.sign == PAUSE:
            return self.sign
        else:
            return self.sign + str(self.octave)


def muslength(fraction_length, bpm):
    'Returns note length in ms for BPM'
    return 60000.0 * fraction_lenght / bpm


def parser(melody, bpm, default_len=1/4):
    melody = melody.strip().replace('\n', ' ').split(' ')
        
    for record in melody:
        if record == '':
            continue
        if '/' in record:
            default_len = Fraction(record) * 60000.0 / bpm
            continue
            
        yield Note(record).freq, int(default_len)
  

def sequencelength(seq, bpm, default_len=1/4):
    melody = melody.strip().replace('\n', ' ').split(' ')
        
    length = 0
    for record in melody:
        if record == '':
            continue
        if '/' in record:
            default_len = Fraction(record) * 60000.0 / bpm
            continue
        length += default_len
        
    return length
    

