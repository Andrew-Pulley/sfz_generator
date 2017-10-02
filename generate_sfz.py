#!/usr/bin/env python

import parse_csv
import midi_note
import keyswitch_functions

def GenerateSfz(
        globalAttributes,
        performanceTypeByKeySwitch,
        csvFileName,
        outputFileName):
    
    sfzRegions = parse_csv.ParseCsv(csvFileName)
    
    outputGroupStrings = []

    if globalAttributes.GetUsesKeySwitch():
        keySwitchNames = performanceTypeByKeySwitch.keys()
        keySwitchMidiNotes = sorted([
            midi_note.MidiNote(keySwitchName) 
            for keySwitchName in keySwitchNames])
        
        for keySwitchMidiNote in keySwitchMidiNotes:
            outputGroupStrings.append(
                keyswitch_functions.CallKeySwitchFunction(
                    performanceTypeByKeySwitch[keySwitchMidiNote.GetAsString()],
                    keySwitchMidiNote.GetAsString(),
                    sfzRegions,
                    globalAttributes.sampleIntervalDistance,
                    globalAttributes.sampleOffsetIsUp,
                    1))
    else:
        # There are no key switches for this instrument
        outputGroupStrings.append(
            keyswitch_functions.GetOutputWithoutKeySwitch(
                sfzRegions,
                globalAttributes.sampleIntervalDistance,
                globalAttributes.sampleOffsetIsUp,
                1))

    with open(outputFileName, 'wb') as sfzFile:
        sfzFile.write(globalAttributes.GetAsString())
        sfzFile.write('\n\n')
        for outputGroupString in outputGroupStrings:
            sfzFile.write(outputGroupString)
            sfzFile.write('\n\n')
    print "Success!"

def CallGenerateSfz(sfzAttributesFile):
    import imp
    import os
    sfzAttributes = imp.load_source(
        os.path.splitext(os.path.basename(sfzAttributesFile))[0],
        sfzAttributesFile)
    
    GenerateSfz(
        sfzAttributes.globalAttributes,
        sfzAttributes.performanceTypeByKeySwitch,
        sfzAttributes.csvFileName,
        sfzAttributes.outputFileName)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        sys.stderr.write('Usage: {} <sfz-attributes-python-script>\n'.format(
            __file__))
        sys.exit(-1)
    
    CallGenerateSfz(sys.argv[1])
