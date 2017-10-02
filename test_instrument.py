import sfz_global
import generate_sfz

"""

Here is where we set all attributes for your SFZ.
Please follow the instructions written in the comments.
Be careful not to delete anything unless specifically told to do so.

"""

# CSV file that contains file names, ins and outs
csvFileName = 'bass_clarinet.csv'

"""
CSV Names should be named as follows:
instrument-vel-roundrobin-articulation-midinote
i.e. flute-p-rr1-stc-c4
Be sure to omit any section of the filename not used.
i.e. if we only had single sustain notes: flute-sus-c4
"""

# Name the SFZ file to be output
outputFileName = 'Bass Clarinet Solo.sfz'

globalAttributes = sfz_global.SfzGlobalAttributes(

# Library Name
    libraryName = 'Sonatina Philharmonic Orchestra',
# Instrument Creator
    creator = 'Andrew Pulley',

# Instrument Type
    instrumentType = 'Bass Clarinet',

#Lowest Keyswitch Note
    loKeySwitchNote = 'a#0',

# Highest Keyswitch Note
    hiKeySwitchNote = 'f1',

#Amp Release
    ampRelease = 0.550,

    # Sample Interval Distance (In Semitones)
    sampleIntervalDistance = 3,

    # Sample Offset - Up or Down represented as True or False
    sampleOffsetIsUp = True,

    # Custom Attributes - insert tutorial
    customAttributes = '\n'.join([
        'fil_veltrack=12000',
        'fil_type=lpf_2p',
        'cutoff=120'])
    )

performanceTypeByKeySwitch = {

    'a#0': 'legDxfStc',
    'c1': 'stc',
    'd1': 'polyLegDxfStc',
    'd#1': 'singlePlayDxfStc',
    'f1': 'legDxfStc'}
