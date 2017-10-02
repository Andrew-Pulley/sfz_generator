class KeySwitchRangeError(RuntimeError):
    pass
    
class SfzGlobalAttributes(object):
    def __init__(self,
            libraryName = None,
            creator = None,
            instrumentType = None,
            loKeySwitchNote = None,
            hiKeySwitchNote = None,
            ampRelease = None,
            sampleIntervalDistance = None,
            sampleOffsetIsUp = None,
            customAttributes = None):
        self.libraryName = libraryName
        self.creator = creator
        self.instrumentType = instrumentType
        self.loKeySwitchNote = loKeySwitchNote
        self.hiKeySwitchNote = hiKeySwitchNote
        self.ampRelease = ampRelease
        self.sampleIntervalDistance = sampleIntervalDistance
        self.sampleOffsetIsUp = sampleOffsetIsUp
        self.customAttributes = customAttributes
        
        if self.loKeySwitchNote and self.hiKeySwitchNote:
            # We are okay. They are both defined
            pass
        elif self.loKeySwitchNote and not self.hiKeySwitchNote:
            raise KeySwitchRangeError(
                "Found loKewSwitchNote, but missing "
                "hiKeySwitchNote from your attributes file")
        elif self.hiKeySwitchNote and not self.loKeySwitchNote:
            raise KeySwitchRangeError(
                "Found hiKewSwitchNote, but missing "
                "loKeySwitchNote from your attributes file")
        else:
            # We are okay. They are both None
            pass
        
# Format the global output
    def GetAsString(self):
        lines = ['// ------------------------------']
        lines.append('// {}'.format(self.libraryName))
        lines.append('// ------------------------------')
        lines.append('// SFZ Created by {}'.format(self.creator))
        lines.append('// ------------------------------')
        lines.append('// {}\n'.format(self.instrumentType))
        lines.append('<global>')
        lines.append('xfin_locc11=0')
        lines.append('xfin_hicc11=127')
        lines.append('off_mode=normal')
        
        if self.GetUsesKeySwitch():
            lines.append('sw_lokey={}'.format(self.loKeySwitchNote))
            lines.append('sw_hikey={}'.format(self.hiKeySwitchNote))
        
        if self.ampRelease is not None:
            lines.append('ampeg_release={}'.format(self.ampRelease))
        
        if self.customAttributes is not None:
            lines.append(self.customAttributes)
        
        lines.append('\n<control>')
        lines.append('label_cc11=Expression')
        lines.append('set_cc11=127')
        return '\n'.join(lines)

    def GetUsesKeySwitch(self):
        return (self.loKeySwitchNote is not None
            and self.hiKeySwitchNote is not None)
