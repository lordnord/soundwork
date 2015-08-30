import wave
import struct

import random
import math


class ReadMono(wave.Wave_read):
    def samples(self):
        for pos in range(self.getnframes()):
            print '\r', pos,
            sample = self.readframes(1)
            yield struct.unpack('<H', sample)[0]
            
class WriteMono(wave.Wave_read):
    pass