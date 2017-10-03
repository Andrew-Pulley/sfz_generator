class GroupSubHeader(object):
    """ ccRange should be a tuple like (0, 127) """
    def __init__(
            self, 
            keySwitchNoteName,
            keySwitchType=None,
            keySwitchLabel=None,
            ccNumber=None,
            ccRange=None,
            indentTabCount=0):
        self.keySwitchNoteName = keySwitchNoteName
        self.keySwitchType = keySwitchType
        self.keySwitchLabel = keySwitchLabel
        self.indentTabCount = indentTabCount
        self.ccNumber = ccNumber
        self.ccRange = ccRange
    
    def GetAsString(self, ccRangeType=None, groupId=None, offByGroupId=None):
        lines = ['<group>']
        
        if groupId is not None:
            lines.append('group={}'.format(groupId))
            
        if offByGroupId is not None:
            lines.append('off_by={}'.format(offByGroupId))
                
        if self.ccNumber is not None:
            assert(ccRangeType is not None)
            lines.append('{}_locc{}={}'.format(
                ccRangeType,
                self.ccNumber,
                self.ccRange[0]))
            lines.append('{}_hicc{}={}'.format(
                ccRangeType,
                self.ccNumber,
                self.ccRange[1]))
        
        if self.keySwitchNoteName is not None:
            assert(self.keySwitchType is not None)
            lines.append('{}={}'.format(
                self.keySwitchType,
                self.keySwitchNoteName))
        
        if self.keySwitchLabel is not None:
            assert(self.keySwitchLabel is not None)
            lines.append('sw_label={}\n'.format(
                self.keySwitchLabel))
        
        return '\n'.join(['\t' * self.indentTabCount + line for line in lines])


def GetHeaderLines(headerName, indentTabCount):
    headerLines = ['// ------------------------------',
        '// {}'.format(headerName),
        '// ------------------------------\n']
       
    return '\n'.join(['\t' * indentTabCount + line for line in headerLines])