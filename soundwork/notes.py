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
OCTAVE = 12
INDEX = 'None C C# D D# E F F# G G# A A# B'.split(' ')

class NotationError(Exception):
    pass

def Note(note):
    if note == PAUSE:
        return PauseNote(note)
    else:
        return ActualNote(note)
    
class PauseNote(object):
    freq = 0
    sign = PAUSE

    def __init__(self, note):
        if note != PAUSE:
            raise ValueError('bad pause note')
    def __str__(self):
        return self.sign
    def up(self):
        'Silently skip impossible action'
    def down(self):
        'Silently skip impossible action'

class ActualNote(object):
    def __init__(self, note):
        if isinstance(note, str):
            self.sign, self.octave = note[:-1], int(note[-1])
        else:
            self.sign, self.octave = note
        self._updatefreq()
        
    def _updatefreq(self):
        self.freq = NOTES[self.sign] / (2 ** (10-self.octave))
        
    def __str__(self):
        return self.sign + str(self.octave)
    
    @property
    def sign(self):
        return INDEX[self.num]
        
    @sign.setter
    def sign(self, newsign):
        self.num = INDEX.index(newsign)
    
    def up(self, num):
        deltanote = num % OCTAVE
        deltaoctave = num // OCTAVE
        
        self.num += deltanote 
        self.octave += deltaoctave
        
    def down(self, num):
        deltanote = num % OCTAVE
        deltaoctave = num // OCTAVE
        
        self.num -= deltanote
        self.octave -= deltaoctave

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
    