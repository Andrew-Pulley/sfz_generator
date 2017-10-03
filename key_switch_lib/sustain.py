# from key_switch_lib.group_sub_header import GroupSubHeader
import key_switch_lib.group_sub_header as gsh

def GetSustain(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = gsh.GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Sustain',
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

    # Fill out sfzOutputStrings
    sfzOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('sus')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        gsh.GetHeaderLines('Sustain', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases)])
    return outputString