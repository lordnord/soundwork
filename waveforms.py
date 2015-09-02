def process(sample, pos):
    
    # Generates a sine wave with frequency = 50 and amplitude = 127.
    freq = 50
    amp = 127
    res = math.sin(math.radians(pos * freq) / qrate) * amp
    
        
    if res > 127:
        res = 127
    elif res < -128:
        res = -128
    return res
