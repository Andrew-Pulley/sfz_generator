from key_switch_lib.group_sub_header import GroupSubHeader, GetHeaderLines
from key_switch_lib.fast_attack import GetFastAttack
from key_switch_lib.sustain import GetSustain


"""-----Sustain Vibrato-----"""
def GetVibrato(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Vibrato',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('vib_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('vib')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Sustain Vibrato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString


"""-----Sustain Deep Vibrato-----"""
def GetDeepVibrato(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Deep Vibrato',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('dvib_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('dvib')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Sustain Deep Vibrato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString

"""-----Smear-----"""
def GetSmear(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Smear',
        indentTabCount=indentTabCount)
    
    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('smear_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('smear')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Smear No Vibrato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString

"""-----Flutter-----"""
def GetFlutter(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Flutter',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('flutter_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('flutter')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Flutter', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString
    
"""-----Flutter Fall-----"""
def GetFlutterFall(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Flutter Fall',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('fltfl_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('fltfl')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Flutter Fall', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString
    
"""-----Fall-----"""
def GetFall(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Fall',
        indentTabCount=indentTabCount)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('fall')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Fall', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    return outputString

"""-----Fast Fall-----"""
def GetFastFall(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Fast Fall',
        indentTabCount=indentTabCount)

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('fast_fall')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Fast Fall', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    return outputString

"""-----Legato DXF Staccato-----"""
def GetLegDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Legato DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('sus_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('sus')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Legato DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout', groupId=1, offByGroupId=1),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin', groupId=2, offByGroupId=2),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Legato DXF Vibrato-----"""
def GetLegDxfVib(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Legato DXF Vibrato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        xfoutOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('sus_rel')
    except KeyError:
        xfoutOutputStringsReleases = []
    else:
        xfoutOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    try:
        xfinOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('vib_rel')
    except KeyError:
        xfinOutputStringsReleases = []
    else:
        xfinOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('sus')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('vib')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Legato DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout', groupId=1, offByGroupId=1),
        '\n\n'.join(xfoutOutputStrings + xfoutOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin', groupId=2, offByGroupId=2),
        '\n\n'.join(xfinOutputStrings + xfinOutputStringsReleases)])
    return outputString

"""-----Detache DXF Staccato-----"""
def GetDetDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Detache DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('det_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('det')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Detache DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout', groupId=1, offByGroupId=1),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin', groupId=2, offByGroupId=2),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Vibrato DXF Staccato-----"""
def GetVibDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Vibrato DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('vib_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('vib')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Detache DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout', groupId=1, offByGroupId=1),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin', groupId=2, offByGroupId=2),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Staccato-----"""
def GetStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Staccato',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Staccato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Slap-----"""
def GetSlap(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Slap',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('slap')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Slap', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Pop-----"""
def GetPop(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Pop',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('pop')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Pop', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Hammer On m2-----"""
def GetHMin(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Minor 2nd Hammer On',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('hmin')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Hammer On m2', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Hammer On M2-----"""
def GetHMaj(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Major 2nd Hammer On',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('hmaj')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Hammer On M2', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Pull Off m2-----"""
def GetPMin(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Minor 2nd Pull Off',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('pmin')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Pull Off m2', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Dive-----"""
def GetDive(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Dive',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('dive')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Dive', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Slide-----"""
def GetSlide(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Slide',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('slide')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Slide', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Staccatisimo-----"""
def GetStcm(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Staccatisimo',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('stcm')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Staccaticimo', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Marcato-----"""
def GetMarc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Marcato',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('marc')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Marcato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Doit-----"""
def GetDoit(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Doit',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('doit')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Doit', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Sforzando-----"""
def GetSforzando(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Sforzando',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('sfz_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('sfz')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Sforzando', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Closed-----"""
def GetClosed(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Closed',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('closed_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('closed')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Closed', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString


"""-----Half-----"""
def GetHalf(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Half',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('half_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('half')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Open', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString


"""-----Wah-----"""
def GetWah(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Wah',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('wah_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('wah')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Wah', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString


"""-----Wop-----"""
def GetWop(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Wop',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('wop')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Wop', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Grace-----"""
def GetGrace(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Grace',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('grace_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('grace')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Grace', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Scoop-----"""
def GetScoop(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Scoop',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('scoop_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('scoop')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Scoop', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Bend-----"""
def GetBend(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Bend',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('bend_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('bend')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Bend', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString


"""-----Polyphonic Legato DXF Staccato-----"""
def GetPolyLegDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Poly Legato DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('sus_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('sus')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Polylegato DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout'),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin'),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Tremolo DXF Staccato-----"""
def GetTremDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Tremolo DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('trem_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)

    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('trem')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Tremolo DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout'),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin'),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Single Play DXF Staccato-----"""
# We use single play if we want samples that contain loopStart and loopEnd to generate without values.
def GetSinglePlayDxfStc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    # return GetHeaderLines('Single Play DXF Staccato', indentTabCount)
    
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='No Loop DXF Staccato',
        ccNumber=1,
        ccRange=(0,127),
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('sus_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out the xfoutOutputStrings and xfinOutputStrings...
    xfoutRegions = sfzRegions.GetSfzRegionArticulationGroup('sus')
    xfinRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    xfoutOutputStrings = xfoutRegions.GetOutputStringsListAsSinglePlay(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    xfinOutputStrings = xfinRegions.GetOutputStringsListAsSinglePlay(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('No Loop DXF Staccato', indentTabCount),
        groupSubHeader.GetAsString(ccRangeType='xfout'),
        '\n\n'.join(xfoutOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(ccRangeType='xfin'),
        '\n\n'.join(xfinOutputStrings)])
    return outputString

"""-----Half Step Trill-----"""
def GetHTrill(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Half Step Trill',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('hst_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('hst')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Half Step Trill', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Whole Step Trill-----"""
def GetWTrill(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Whole Step Trill',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('wst_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('wst')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Whole Step Trill', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Shake-----"""
def GetShake(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Shake',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('shake_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('shake')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Shake', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString


"""-----Tremolo-----"""
def GetTrem(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Tremolo',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('trem_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('trem')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Tremolo', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Ponticello Tremolo-----"""
def GetPont(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Ponticello Tremolo',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('pont_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('pont')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Pontiecello Tremolo', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Harmonics-----"""
def GetHarm(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Harmonics',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('harm_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('harm')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Harmonics', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString

"""-----Sliding Harmonics-----"""
def GetSHarm(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Sliding Harmonics',
        indentTabCount=indentTabCount)

    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('sl_harm')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Sliding Harmonics', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Detache-----"""
def GetDetache(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Detache',
        indentTabCount=indentTabCount)

    try:
        sfzOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('det_rel')
    except KeyError:
        sfzOutputStringsReleases = []
    else:
        sfzOutputStringsReleases = sfzOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('det')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Detache', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    
    return outputString
    
"""-----Pizzicato-----"""
def GetPizz(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Pizzicato',
        indentTabCount=indentTabCount)

    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('piz')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Pizzicato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString
    
"""-----Spiccato-----"""
def GetSpc(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Spiccato',
        indentTabCount=indentTabCount)

    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('spc')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Spiccato', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString

"""-----Rip-----"""
def GetRip(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Rip',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('rip')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Grace', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Release-----"""
def GetRel(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Release',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('rel')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Releases', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


"""-----Fret Noise-----"""
def GetFret(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):
    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchLabel='Fret Noise',
        indentTabCount=indentTabCount)
    
    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('fret')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Fret Noises', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings)])
    
    return outputString


    """-----Default Action (No Keyswitches Present)-----"""
def GetOutputWithoutKeySwitch(
        sfzRegions,
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount=0):
        
    defaultArticulationType = 'spu'

    groupSubHeader = GroupSubHeader(
        keySwitchNoteName=None,
        keySwitchType=None,
        indentTabCount=indentTabCount)

    defaultOutputRegions = sfzRegions.GetSfzRegionArticulationGroup(
        defaultArticulationType)
    
    try:
        defaultSPDOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('spd')
    except KeyError:
        defaultSPDOutputStrings = []
    else:
        defaultSPDOutputStrings = defaultSPDOutputRegions.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    try:
        defaultOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('rel')
    except KeyError:
        defaultOutputStringsReleases = []
    else:
        defaultOutputStringsReleases = defaultOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
        
    try:
        defaultHammerOutputRegionsReleases = sfzRegions.GetSfzRegionArticulationGroup('ham_rel')
    except KeyError:
        defaultHammerOutputStringsReleases = []
    else:
        defaultHammerOutputStringsReleases = defaultHammerOutputRegionsReleases.GetOutputStringsList(
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount + 1)
    
    defaultOutputStrings = defaultOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        GetHeaderLines('Sus Ped Up', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(defaultOutputStrings \
        + defaultOutputStringsReleases \
        + defaultHammerOutputStringsReleases),
        '\n',
        GetHeaderLines('Sus Ped Down', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(defaultSPDOutputStrings)])

    return outputString


keySwitchFunctionsByPerformanceType = {
	'sustain': GetSustain,
	'sforzando': GetSforzando,
	'vibrato': GetVibrato,
	'deepVibrato': GetDeepVibrato,
	'fastAttack': GetFastAttack,
	'smear': GetSmear,
	'flutter': GetFlutter,
	'flutterFall': GetFlutterFall,
	'fall': GetFall,
	'fastFall': GetFastFall,
	'legDxfStc': GetLegDxfStc,
	'legDxfVib': GetLegDxfVib,
	'tremDxfStc': GetTremDxfStc,
	'stc': GetStc,
	'slap': GetSlap,
	'pop': GetPop,
	'hmin': GetHMin,
	'pmin': GetPMin,
	'dive': GetDive,
	'slide': GetSlide,
	'stcm': GetStcm,
	'marc': GetMarc,
	'doit': GetDoit,
	'grace': GetGrace,
	'scoop': GetScoop,
	'bend': GetBend,
	'polyLegDxfStc': GetPolyLegDxfStc,
	'detDxfStc': GetDetDxfStc,
	'closed': GetClosed,
	'half': GetHalf,
	'wah': GetWah,
	'wop': GetWop,
	'hTrill': GetHTrill,
	'wTrill': GetWTrill,
	'shake': GetShake,
	'trem': GetTrem,
	'pont': GetPont,
	'harm': GetHarm,
	'sHarm': GetSHarm,
	'detache': GetDetache,
	'pizz': GetPizz,
	'spc': GetSpc,
	'rip': GetRip,
	'rel': GetRel,
	'fret': GetFret}

 
def CallKeySwitchFunction(
        performanceType,
        keySwitchNoteName,
        sfzRegions,
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount):
        
    keySwitchFunction = keySwitchFunctionsByPerformanceType[performanceType]
    return keySwitchFunction(
        keySwitchNoteName,
        sfzRegions,
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount)
