# coding: utf8
import wave
import struct

import random
import math

class Mono:
    FORMATS = (None, 'B', 'H') # 8bit or 16bit
    
    @property
    def format(self):
        return '<' + self.FORMATS[self._sampwidth]
        
    @property
    def max(self):
        return 2 ** (8 ** self.getsampwidth() - 1)


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
        
    def bytesample(self, intsample):
        return struct.pack(self.format, intsample + self.max)
        
    def gen(self, process):
        for pos in range(self._nframes):
            sample = process(pos)
            self.writeframes(self.bytesample(sample))
            
    def writefromfile(self, file, process):
        for pos, sample in enumerate(file.getsamples()):
            out = process(sample, pos)
            self.writeframes(self.bytesample(out))
