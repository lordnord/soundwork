# coding: utf8
import wave
import struct

import random
import math

class Mono:
    @property
    def max(self):
        return 2 ** (8 ** self.getsampwidth() - 1)


class ReadMono(wave.Wave_read, Mono):
    format = (None, 'B', 'H') # 8bit or 16bit
    def getsamples(self, number=1):
        # когда number > 1 последняя порция может быть с неправильной длиной
        # сейчас чтобы этого не происходило количество семплов должно
        # делиться на number без остатка
        for pos in range(self.getnframes() / number):
            samples = self.readframes(number)
            format = self.format[self.getsampwidth()]
            yield struct.unpack('<' + format*number, samples)
            
            
class WriteMono(wave.Wave_write):
    def gen(self, process, number=1):
        for pos in range(self.getnframes()):
            data =  struct.unpack('<' + format*number, samples)
            self.writeframes()
            
    def fromfile(self, file, process, number=1):
        for samples in file.getsamples(number):
            # тут чтение по порциям тоже вызывает проблемы
            # надо вычитать из каждого числа/семпла в списке 128 (32768)
            
            out = process((i - file.max for i in samples), pos) # и потом прибавлять.
