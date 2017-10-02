velocityLayerNames = (
   'pppp',
   'ppp',
   'pp',
   'p',
   'mp',
   'mf',
   'f',
   'ff',
   'fff',
   'ffff')


def CompareVelocityLayers(layer1, layer2):
    # https://docs.python.org/2/library/functions.html#cmp
    return cmp(
        velocityLayerNames.index(layer1),
        velocityLayerNames.index(layer2))


def GetSortedVelocityLayerNames(velocityLayers):
    # https://docs.python.org/2/library/functions.html#sorted
    return sorted(velocityLayers, cmp=CompareVelocityLayers)


def GetVelocityLayerRanges(velocityLayerCount):
    # I have chosen to evenly divide the velocity range by the number of
    # velocity layers, without giving any weight to individual velocities.
    layerWidth = 127.0 / velocityLayerCount
    result = []
    for i in range(velocityLayerCount - 1):
        result.append((
            int(round(i * layerWidth)),
            int(round((i + 1) * layerWidth - 1))))
    result.append((
        int(round((velocityLayerCount - 1) * layerWidth)),
        int(round(((velocityLayerCount - 1) + 1) * layerWidth))))
    return result


def ValidateGetVelocityLayerRanges():
    """
    Note: This test method uses the line continuation character '\' which
    tells python that all of the code on the next visual line belongs to the
    same logical line.

    To see this run in the interpreter:
    >>> import velocity_layer 
    >>> velocity_layer.ValidateGetVelocityLayerRanges()
    """
    
    for velocityLayerCount in range(1, len(velocityLayerNames) + 1):
        print 'Checking GetVelocityLayerRanges({})'.format(velocityLayerCount)
        velocityLayerRanges = GetVelocityLayerRanges(velocityLayerCount)
        assert(len(velocityLayerRanges) == velocityLayerCount)
        for index, velocityRange in enumerate(velocityLayerRanges):
            print "  Validating range {}".format(velocityRange)
            if index == 0:
                # This is the lowest velocity range
                assert velocityRange[0] == 0, "The range must extend down to 0."
            else:
                assert \
                    velocityRange[0] - velocityLayerRanges[index - 1][1] == 1, \
                    "Each range must be separated by 1."
                if index == (velocityLayerCount - 1):
                    # This is the last velocity layer range
                    assert \
                        velocityRange[1] == 127, \
                        "The range must extend up to 127."

class VelocityLayers(set):
    def __init__(self, *args):
        super(VelocityLayers, self).__init__(*args)
        self.__velocityRangeByVelocityLayerName = None

    # Override of add method
    def add(self, addedVelocityLayer):
        assert(addedVelocityLayer in velocityLayerNames)
        
        # Invalid the calculated velocity layers
        self.__velocityRangeByVelocityLayerName = None

        super(VelocityLayers, self).add(addedVelocityLayer)

    # Private Method
    def __CalculateVelocityLayers(self):
        assert len(self), "There are no velocity layers."
        self.__velocityRangeByVelocityLayerName = {}
        sortedVelocityLayerNames = GetSortedVelocityLayerNames(self)
        velocityLayerRanges = GetVelocityLayerRanges(
            len(sortedVelocityLayerNames))

        for index, velocityLayerName in enumerate(sortedVelocityLayerNames):
            self.__velocityRangeByVelocityLayerName[velocityLayerName] = \
                velocityLayerRanges[index]

    # Public Method
    def GetVelocityRange(self, velocityLayerName):
        if self.__velocityRangeByVelocityLayerName is None:
            self.__CalculateVelocityLayers()

        return self.__velocityRangeByVelocityLayerName[velocityLayerName]
