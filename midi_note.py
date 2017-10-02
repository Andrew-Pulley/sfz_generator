#Create note dictionaries
indexByPitchName = {
    'c': 0,
    'c#': 1,
    'd': 2,
    'd#': 3,
    'e': 4,
    'f': 5,
    'f#': 6,
    'g': 7,
    'g#': 8,
    'a': 9,
    'a#': 10,
    'b': 11}

pitchNameByIndex = {
    0: 'c',
    1: 'c#',
    2: 'd',
    3: 'd#',
    4: 'e',
    5: 'f',
    6: 'f#',
    7: 'g',
    8: 'g#',
    9: 'a',
    10: 'a#',
    11: 'b'}

class MidiNote(object):
    def __init__(self, midiNoteAsString):
        self.octaveIndex = int(midiNoteAsString[-1])
        self.noteIndex = indexByPitchName[midiNoteAsString[:-1].lower()]
    
    def GetAsString(self, offset=0):
        transposedNoteIndex = self.noteIndex + offset
        if transposedNoteIndex < 0:
            transposedOctaveIndex = self.octaveIndex - 1
        elif transposedNoteIndex > 11:
            transposedOctaveIndex = self.octaveIndex + 1
        else:
            transposedOctaveIndex = self.octaveIndex
        transposedPitchName = pitchNameByIndex[transposedNoteIndex % 12]
        
        return '{}{}'.format(transposedPitchName, transposedOctaveIndex)
    
    def GetFullNoteIndex(self):
        return self.octaveIndex * 12 + self.noteIndex
        
    def __lt__(self, other):
            return self.GetFullNoteIndex() < other.GetFullNoteIndex()
    
    def __gt__(self, other):
        return self.GetFullNoteIndex() > other.GetFullNoteIndex()
    
    def __le__(self, other):
        return not self.__gt__(other)
    
    def __ge__(self, other):
        return not self.__lt__(other)
    
    def __eq__(self, other):
        return (self.octaveIndex == other.octaveIndex
            and self.noteIndex == other.noteIndex)
    
    def __ne__(self, other):
        return not self.__eq__(other)
        
    def __repr__(self):
       return "MidiNote('{}')".format(self.GetAsString())

    def __hash__(self):
        return hash((self.octaveIndex, self.noteIndex)) 
