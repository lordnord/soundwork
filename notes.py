
def muslength(l, bpm=None):
    # Returns note length in ms for BPM
    if bpm == None:
        bpm = muslength.last
    measure = 60000.0 / bpm
    return measure * l

muslength.last = 70


# Note frequencies for 10th octave
notes = {
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
