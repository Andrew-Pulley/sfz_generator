import midi_note

class CsvParseError(RuntimeError):
    pass

class MissingHiKey(CsvParseError):
    pass
    
class MissingLoopEnd(CsvParseError):
    pass

articulationTypeByAbbreviation = {
    'sus': 'sustain',
    'stc': 'staccato',
    'piz': 'pizzicato',
    'trem': 'tremolo',
    'tr1': 'halfTrill',
    'tr2': 'wholeTrill',
    'sfz': 'sforzando'
    }

velocityLayerNames = (
   'pppp',
   'ppp',
   'pp',
   'p',
   'mf',
   'f',
   'ff',
   'fff'
   'ffff')
   
class SfzRegion(object):
    def __init__(self, csvRow):
        self.sampleFileName = csvRow[0]
        self.ParseSampleFileName()
        
        self.loopStart = None
        self.loopEnd = None
        try:
            self.loopStart = int(csvRow[1])
        except IndexError:
            # The csvRow only has one item, the sampleFileName
            # Create default parameters
            self.CreateDefaultRange()
            
        except ValueError:
            # The csvRow as an additional item, but it is not an integer.
            # Assume that it is a custom note range.
            self.loKeyAsString = csvRow[1]
            self.hiKeyAsString = csvRow[2]
            try:
                self.hiKeyAsString = csvRow[2]
            except IndexError:
                #Raise our own exception to say what happened.
                raise MissingHiKey(
                    "Only one key value was entered. "
                    "Please include both lowkey and hikey values.")
            
        else:
            # We successfully got a loopStart value.
            # Assume there is a loop end value
            try:
                self.loopEnd = int(csvRow[2]) - 1
            except (IndexError, ValueError):
                # The loopEnd does not exist, or it is not an integer
                raise MissingLoopEnd("Found loopStart, but missing loopEnd")
            try:
                self.loKeyAsString = csvRow[3]
            except IndexError:
                # There was no custom loKey in the csv row
                self.CreateDefaultRange()
            else:
                # We found a loKey in the csvRow
                #Assume that there is also a hiKey
                try:
                    self.hiKeyAsString = csvRow[4]
                except IndexError:
                    raise MissingHiKey(
                        "Only one key value was entered. "
                        "Please include both lowkey and hikey values.")         
    
    def CreateDefaultRange(self):
        self.loKeyAsString = self.pitchKeyCenter.GetAsString(-1)
        self.hiKeyAsString = self.pitchKeyCenter.GetAsString(1)

    def ParseSampleFileName(self):
        # file naming convention instrument-vel-roundrobin-articulation-midinote.wav    
        parts = self.sampleFileName.split('-')
        self.instrumentName = parts[0]

        self.velocityLayer = None
        self.roundRobinIndex = None
        
        for part in parts[1:-2]:
            if part in velocityLayerNames:
                self.velocityLayer = part
            elif part.startswith('rr'): 
                self.roundRobinIndex = int(part[2:])
        self.pitchKeyCenter = midi_note.MidiNote(parts[-1])
        self.articulationType = parts[-2]

    def GetIsVelocityLayer(self):
        return self.velocityLayer is not None
        
    def GetIsRoundRobin(self):
        return self.roundRobinIndex is not None
                
    def GetIsLoopedSample(self):
        return (self.loopStart is not None) and (self.loopEnd is not None)

    def GetAsString(self, indentTabCount=1):
        lines = ['<region>']
        lines.append('sample=Samples\\{}.wav'.format(self.sampleFileName))
        lines.append('lokey={}'.format(self.loKeyAsString))
        lines.append('hikey={}'.format(self.hiKeyAsString))
        if self.GetIsLoopedSample():
            lines.append('loop_mode=loop_continuous')
            lines.append('loop_start={}'.format(self.loopStart))
            lines.append('loop_end={}'.format(self.loopEnd))
            
        lines.append('pitch_keycenter={}'.format(
            self.pitchKeyCenter.GetAsString()))
        
        return '\n' .join(['\t' * indentTabCount + line for line in lines])
        
    def GetAsStringSinglePlay(self, indentTabCount=1):
        lines = ['<region>']
        lines.append('sample=Samples\\{}.wav'.format(self.sampleFileName))
        lines.append('lokey={}'.format(self.loKeyAsString))
        lines.append('hikey={}'.format(self.hiKeyAsString))
        lines.append('pitch_keycenter={}'.format(
            self.pitchKeyCenter.GetAsString()))
            
        return '\n' .join(['\t' * indentTabCount + line for line in lines])
