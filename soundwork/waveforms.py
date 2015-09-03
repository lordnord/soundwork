from __future__ import division
import math
import random

def sine(freq):
    def wrapped(file, pos):
        w = (2 * math.pi * freq) / file.getframerate()
        res = math.sin(pos * w) * file.amplit(100)
        return int(res)
    return wrapped

def square(freq):
    def wrapped(file, pos):
        return None
    return wrapped
    
def triangular(freq):
    def wrapped(file, pos):
        return None
    return wrapped
    
def sawtooth(freq):
    def wrapped(file, pos):
        return None
    return wrapped
    
def noise(file, pos):
    return random.randrange(-file.max, file.max)
    
def zfill(file, pos):
    return 0
    
def merge(*funcs):
    'Merge results of calls by arithmetic mean.'
    def wrapped(file, pos):
        all = [func(file, pos) for func in funcs]
        return int(sum(all) / len(all))
    return wrapped