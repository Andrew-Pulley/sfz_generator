import midi_note
import velocity_layers

from collections import defaultdict


class CsvParseError(RuntimeError):
    pass


class MissingHiKey(CsvParseError):
    pass


class MissingLoopEnd(CsvParseError):
    pass

class MissingVelocityLayer(CsvParseError):
    pass

articulationTypeByAbbreviation = {
    'sus': 'sustain',
    'spu': 'sustainPedalUp',
    'stc': 'staccato',
    'piz': 'pizzicato',
    'trem': 'tremolo',
    'tr1': 'halfTrill',
    'tr2': 'wholeTrill',
    'sfz': 'sforzando',
    'roll': 'roll',
    'rel': 'release'}

class SfzRegion(object):
    def __init__(self, csvRow):
        self.sampleFileName = csvRow[0]
        self.ParseSampleFileName()
        self.loopStart = None
        self.loopEnd = None
        self.loKeyAsString = None
        self.hiKeyAsString = None
        self.loVelAsString = None
        self.hiVelAsString = None
        try:
            self.loopStart = int(csvRow[1])
        except IndexError:
            # The csvRow only has one item, the sampleFileName
            # Create default parameters
            pass

        except ValueError:
            # The csvRow has an additional item, but it is not an integer.
            # Assume that it is a custom note range.
            self.loKeyAsString = csvRow[1]
            self.hiKeyAsString = csvRow[2]
            try:
                self.hiKeyAsString = csvRow[2]
            except IndexError:
                #Raise our own exception to say what happened.
                raise MissingHiKey(
                    "Only one key value was entered. "
                    "Please include both lokey and hikey values.")

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
                pass
            else:
                # We found a loKey in the csvRow
                #Assume that there is also a hiKey
                try:
                    self.hiKeyAsString = csvRow[4]
                except IndexError:
                    raise MissingHiKey(
                        "Only one key value was entered. "
                        "Please include both lokey and hikey values.")

    def CreateDefaultRange(self, sampleIntervalDistance, sampleOffsetIsUp):
        if sampleIntervalDistance < 2:
            return

        if self.loKeyAsString is not None and self.hiKeyAsString is not None:
            #Nothing to do
            return
        assert self.loKeyAsString is None
        assert self.hiKeyAsString is None

        midIntervalDistance = sampleIntervalDistance / 2

        isSampleIntervalDistanceOdd = sampleIntervalDistance % 2


        if isSampleIntervalDistanceOdd:
            self.loKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance * -1)
            self.hiKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance)
        else:
                # The sampleIntervalDistance is even, so will be spaced unevenly around the pitchKeyCenter.
            if sampleOffsetIsUp:
                self.loKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance * -1 + 1)
                self.hiKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance)
            else:
                self.loKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance * -1)
                self.hiKeyAsString = self.pitchKeyCenter.GetAsString(midIntervalDistance - 1)

    def ParseSampleFileName(self):
        # File naming convention: instrument-velocity-roundrobin-articulation-midinote.wav
        # Required elements: instrument-articulation-midinote
        parts = self.sampleFileName.split('-')
        self.instrumentName = parts[0]

        self.velocityLayer = None
        self.roundRobinIndex = None

        for part in parts[1:-2]:
            if part in velocity_layers.velocityLayerNames:
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

    def GetAsString(
            self,
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount=1,
            lovel=None,
            hivel=None,
            maxRoundRobinIndex=None):
        self.CreateDefaultRange(sampleIntervalDistance, sampleOffsetIsUp)
        lines = ['<region>']
        lines.append('sample=Samples\\{}.wav'.format(self.sampleFileName))
        if sampleIntervalDistance > 1:
            lines.append('pitch_keycenter={}'.format(
                self.pitchKeyCenter.GetAsString()))
            lines.append('lokey={}'.format(self.loKeyAsString))
            lines.append('hikey={}'.format(self.hiKeyAsString))
        elif sampleIntervalDistance == 1:
            lines.append('key={}'.format(
                self.pitchKeyCenter.GetAsString()))
        if lovel is not None and hivel is not None:
            lines.append('lovel={}'.format(lovel))
            lines.append('hivel={}'.format(hivel))
        if self.GetIsLoopedSample():
            lines.append('loop_mode=loop_continuous')
            lines.append('loop_start={}'.format(self.loopStart))
            lines.append('loop_end={}'.format(self.loopEnd))
        if self.GetIsRoundRobin():
            if maxRoundRobinIndex is None:
                raise ValueError("Round Robin sample requires maxRoundRobinIndex")
            lines.append('seq_length={}'.format(maxRoundRobinIndex))
            lines.append('seq_position={}'.format(self.roundRobinIndex))
        if self.articulationType == 'rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'sus_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'det_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'trem_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'wst_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'hst_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'harm_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'trill_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'pont_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')
        elif self.articulationType == 'vib_rel':
            lines.append('trigger=release')
            lines.append('ampeg_attack=.55')

        return '\n' .join(['\t' * indentTabCount + line for line in lines])

    def GetAsStringSinglePlay(
            self,
            sampleIntervalDistance,
            sampleOffsetIsUp,
            indentTabCount=1,
            lovel=None,
            hivel=None,
            maxRoundRobinIndex=None):
        self.CreateDefaultRange(sampleIntervalDistance, sampleOffsetIsUp)
        lines = ['<region>']
        lines.append('sample=Samples\\{}.wav'.format(self.sampleFileName))
        lines.append('pitch_keycenter={}'.format(
            self.pitchKeyCenter.GetAsString()))
        if sampleIntervalDistance > 1:
            lines.append('lokey={}'.format(self.loKeyAsString))
            lines.append('hikey={}'.format(self.hiKeyAsString))
        if lovel is not None and hivel is not None:
            lines.append('lovel={}'.format(lovel))
            lines.append('hivel={}'.format(hivel))
        if self.GetIsRoundRobin():
            if maxRoundRobinIndex is None:
                raise ValueError("Round Robin sample requires maxRoundRobinIndex")
            lines.append('seq_length={}'.format(maxRoundRobinIndex))
            lines.append('seq_position={}'.format(self.roundRobinIndex))

        return '\n' .join(['\t' * indentTabCount + line for line in lines])

    def __repr__(self):
        return 'SfzRegion(pitchKeyCenter={}, sampleFileName={})'.format(
            self.pitchKeyCenter,
            self.sampleFileName)


def GetSfzRegionString(sfzRegion, *args, **kwargs):
    return sfzRegion.GetAsString(*args, **kwargs)

def GetSfzRegionStringAsSinglePlay(sfzRegion, *args, **kwargs):
    return sfzRegion.GetAsStringSinglePlay(*args, **kwargs)

def GetMaxRoundRobinIndexByVelocityLayer(sfzRegionList):
    maxRoundRobinIndexByVelocityLayer = {}
    for sfzRegion in sfzRegionList:
        if sfzRegion.GetIsRoundRobin():
            if sfzRegion.GetIsVelocityLayer():
                maxRoundRobinIndexByVelocityLayer[sfzRegion.velocityLayer] = \
                    max(
                        maxRoundRobinIndexByVelocityLayer.get(
                            sfzRegion.velocityLayer,
                            0),
                        sfzRegion.roundRobinIndex)
            else:
                maxRoundRobinIndexByVelocityLayer['NoLayer'] = \
                    max(
                        maxRoundRobinIndexByVelocityLayer.get('NoLayer', 0),
                        sfzRegion.roundRobinIndex)

    return maxRoundRobinIndexByVelocityLayer

class SfzRegionArticulationGroup(list):
    def __init__(self, *args):
        self.articulationType = None
        # self.velocityLayers = velocity_layers.VelocityLayers()
        self.velocityLayersByPitchKeyCenter = defaultdict(velocity_layers.VelocityLayers)
        self.sfzRegionListByPitchKeyCenter = defaultdict(list)
        super(SfzRegionArticulationGroup, self).__init__(*args)

    def append(self, sfzRegion):
        if self.articulationType is None:
            self.articulationType = sfzRegion.articulationType
        else:
            assert(sfzRegion.articulationType == self.articulationType)

        if sfzRegion.GetIsVelocityLayer():
            # self.velocityLayers.add(sfzRegion.velocityLayer)
            self.velocityLayersByPitchKeyCenter[sfzRegion.pitchKeyCenter].add(sfzRegion.velocityLayer)
            
        self.sfzRegionListByPitchKeyCenter[sfzRegion.pitchKeyCenter].append(
            sfzRegion)

        super(SfzRegionArticulationGroup, self).append(sfzRegion)

    def __GetOutputStringsList(
            self,
            outputMethod,
            *args,
            **kwargs):

        outputStrings = []
        for pitchKeyCenter in \
                sorted(self.sfzRegionListByPitchKeyCenter.keys()):
            sfzRegionList = self.sfzRegionListByPitchKeyCenter[pitchKeyCenter]

            maxRoundRobinIndexByVelocityLayer = \
                GetMaxRoundRobinIndexByVelocityLayer(sfzRegionList)

            for sfzRegion in sfzRegionList:
                maxRoundRobinIndex = None
                if sfzRegion.GetIsVelocityLayer():
                    # lovel, hivel = self.velocityLayers.GetVelocityRange(
                        # sfzRegion.velocityLayer)
                    lovel, hivel = \
                        self.velocityLayersByPitchKeyCenter[sfzRegion.pitchKeyCenter].GetVelocityRange(sfzRegion.velocityLayer)
                    if sfzRegion.GetIsRoundRobin():
                        maxRoundRobinIndex = \
                            maxRoundRobinIndexByVelocityLayer[
                                sfzRegion.velocityLayer]
                else:
                    lovel, hivel = (None, None)
                    if sfzRegion.GetIsRoundRobin():
                        maxRoundRobinIndex = \
                            maxRoundRobinIndexByVelocityLayer['NoLayer']
                kwargs['lovel'] = lovel
                kwargs['hivel'] = hivel
                kwargs['maxRoundRobinIndex'] = maxRoundRobinIndex
                outputStrings.append(outputMethod(sfzRegion, *args, **kwargs))

        return outputStrings


    def GetOutputStringsList(self, *args, **kwargs):
        return self.__GetOutputStringsList(GetSfzRegionString, *args, **kwargs)

    def GetOutputStringsListAsSinglePlay(self, *args, **kwargs):
        return self.__GetOutputStringsList(
            GetSfzRegionStringAsSinglePlay,
            *args,
            **kwargs)

    def GetHasVelocityLayers(self):
        return len(self.velocityLayers)

    def ValidateVelocityLayers(self):
        """Check that there are the same velocity layers present for each
        pitchKeyCenter. Raise an error if there are any missing.

        If this is a non-critical error, you can print out a warning instead."""

        if not self.GetHasVelocityLayers():
            return

        for pitchKeyCenter, sfzRegionList in \
                self.sfzRegionListByPitchKeyCenter.iteritems():
            velocityLayersAtSinglePitch = set()

            for sfzRegion in sfzRegionList:
                if sfzRegion.GetIsVelocityLayer():
                    velocityLayersAtSinglePitch.add(sfzRegion.velocityLayer)

            if velocityLayersAtSinglePitch != self.velocityLayers:
                raise MissingVelocityLayer(
                    "{} are missing for {}.".format(
                        self.velocityLayers.difference(
                            velocityLayersAtSinglePitch),
                        pitchKeyCenter))


class SfzRegions(object):
    def __init__(self, sfzRegionList):
        self.sfzRegionList = sfzRegionList

        # We need a dict that maps articulation types to lists of SfzRegion's
        # that all have the same type.
        # So that we avoid having to check for existing keys every time, we
        # will use the defaultdict class defined in collections.
        # When you access a key that does not exist, it uses its default
        # factory to create the missing value, and inserts it into the dict.
        # All other functionality is the same as the standard dict class.
        # https://docs.python.org/2/library/collections.html#collections.defaultdict
        self.sfzRegionArticulationGroupByArticulationType = defaultdict(
            SfzRegionArticulationGroup)

        for sfzRegion in self.sfzRegionList:
            self.sfzRegionArticulationGroupByArticulationType[
                sfzRegion.articulationType].append(sfzRegion)

        """ for \
                sfzRegionArticulationGroup in \
                self.sfzRegionArticulationGroupByArticulationType.itervalues():
            sfzRegionArticulationGroup.ValidateVelocityLayers() """

    def GetArticulationTypes(self):
        return self.sfzRegionArticulationGroupByArticulationType.keys()

    def GetHasArticulationType(self, articulationType):
        return articulationType in self.GetArticulationTypes()

    def GetAllSfzRegions(self):
        return self.sfzRegionList

    def GetSfzRegionArticulationGroup(self, articulationType):
        if not self.GetHasArticulationType(articulationType):
            raise KeyError(
                "Articulation {} not found.".format(articulationType))

        return self.sfzRegionArticulationGroupByArticulationType[
            articulationType]
