# coding: utf8
import wave
import struct

from . import waveforms
from . import notes

class Mono:
    FORMATS = (None, 'B', 'H') # 8bit or 16bit
            
    def after_init(self):
        self.max = 2 ** (8 ** self._sampwidth - 1)
        self.format = '<' + self.FORMATS[self._sampwidth]

    def amplit(self, percent):
        out = percent * (self.max - 1)/100.0
        return int(out)


class ReadMono(wave.Wave_read, Mono):
    def __init__(self, *args):
        wave.Wave_read.__init__(self, *args)
        self.after_init()
        
    def intsample(self, bytesample):
        return struct.unpack(self.format, bytesample)[0] - self.max

    def getsamples(self):
        for pos in range(self._nframes):
            sample = self.readframes(1)
            yield self.intsample(sample)

    def getwaves(self):
        for pos in range(self._nframes):
            pass

            
class WriteMono(wave.Wave_write, Mono):
    def set(self, bit=None, samplerate=None, file=None):
        if file:
            self.setparams(file.getparams())
        else:
            xparams = (
                1,       # self._nchannels
                bit / 8, # self._sampwidth
                samplerate,
                0,       # self._nframes
                'NONE',
                'not compressed',
                )
            self.setparams(xparams)
            self.after_init()

    def bytesample(self, intsample):
        return struct.pack(self.format, intsample + self.max)
        
    def gen(self, process, msec=0):
        if not msec:
            nsamples = self._nframes - self.tell()
        else:
            nsamples = msec * self.getframerate() / 1000
            print nsamples
        frames = [self.bytesample(process(self, pos)) for pos in range(nsamples)]
        self.writeframes(''.join(frames))
            
    def writefromfile(self, file, process):
        for pos, sample in enumerate(file.getsamples()):
            out = process(self, sample, pos)
            self.writeframes(self.bytesample(out))
            
    def fromnotes(self, seq, waves, bpm=None):
        'High level interface.'
        one_wave = len(waves) == 2 and isinstance(waves[1], int)
        for freq, length in notes.parser(seq, bpm):
            if one_wave:
                print 'one'
                form, coef = waves
                merged = form(freq * coef)
            else:
                print 'many' 
                # list of waves
                freq_waves = tuple(form(freq * coef) for form, coef in waves)
                merged = waveforms.merge(*freq_waves)
            self.gen(merged, length)

            
            
def open(filepath, mode):
    if mode == 'r':
        return ReadMono(filepath)
    elif mode == 'w':
        return WriteMono(filepath)
    else:
        raise ValueError('mode must be "r" or "w"')