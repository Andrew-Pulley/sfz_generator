# from key_switch_lib.group_sub_header import GroupSubHeader
import key_switch_lib.group_sub_header as gsh

def GetFastAttack(keySwitchNoteName, sfzRegions, sampleIntervalDistance, sampleOffsetIsUp, indentTabCount=0):

    groupSubHeader = gsh.GroupSubHeader(
        keySwitchNoteName=keySwitchNoteName,
        keySwitchType='sw_last',
        keySwitchLabel='Fast Attack',
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
    attackOutputRegions = sfzRegions.GetSfzRegionArticulationGroup('stc')
    
    sfzOutputStrings = sfzOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)
        
    attackOutputStrings = attackOutputRegions.GetOutputStringsList(
        sampleIntervalDistance,
        sampleOffsetIsUp,
        indentTabCount + 1)

    outputString = '\n'.join([
        gsh.GetHeaderLines('Fast Attack', indentTabCount),
        groupSubHeader.GetAsString(),
        '\n\n'.join(sfzOutputStrings + sfzOutputStringsReleases),
        '',
        groupSubHeader.GetAsString(),
        '\n\n'.join(attackOutputStrings)])
    
    return outputString