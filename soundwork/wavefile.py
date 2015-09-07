# coding: utf8
import wave
import struct


class Mono:
    FORMATS = (None, 'B', 'H') # 8bit or 16bit
    
    def hardclip(process):
        def _f(*args):
            pass
            
    @property
    def format(self):
        return '<' + self.FORMATS[self._sampwidth]
        
    @property
    def max(self):
        return 2 ** (8 ** self.getsampwidth() - 1)
        
    def amplit(self, percent):
        out = percent * (self.max - 1)/100.0
        return int(out)


class ReadMono(wave.Wave_read, Mono):
    
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
    def set(self, *params, **kw):
        if kw:
            self.setparams(kw['file'].getparams())
        else:
            bit, samplerate, msec = params
            xparams = (
                1,       # self._nchannels
                bit / 8, # self._nsampwidth
                samplerate,
                0, # self._nframes
                'NONE',
                'not compressed',
                )
            self.setparams(xparams)

    def bytesample(self, intsample):
        return struct.pack(self.format, intsample + self.max)
        
    def gen(self, process, msec=0):
        if not msec:
            nsamples = self._nframes - self.tell()
        else:
            nsamples = msec * self.getframerate() / 1000
            print nsamples
        for pos in range(nsamples):
            sample = process(self, pos)
            self.writeframes(self.bytesample(sample))
            
    def writefromfile(self, file, process):
        for pos, sample in enumerate(file.getsamples()):
            out = process(self, sample, pos)
            self.writeframes(self.bytesample(out))

            
            
def open(filepath, mode):
    if mode == 'r':
        return ReadMono(filepath)
    elif mode == 'w':
        return WriteMono(filepath)
    else:
        raise ValueError('mode must be "r" or "w"')