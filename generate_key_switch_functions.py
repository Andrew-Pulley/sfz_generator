import os

filePath = 'key-switch-functions'


def generateKeySwitchFunctions():
    keySwitchFunctionsByPerformanceType = {}
    keySwitchFunctions = []
    for root, dir, files in os.walk(filePath):
        for file in files:
            fileName, fileExtension = os.path.splitext(file)
        
            # Is fileExtension .sfz?
            if fileExtension == '.py':
                # Add to the dictionary keySwitchFunctionsByPerformanceType.
                fileNameElements = fileName.split('-')
                # Make key
                keySwitchFunctionKey = \
                    ''.join([element[0].upper() + element[1:].lower() \
                    for element in fileNameElements])
                keySwitchFunctionKey = \
                    keySwitchFunctionKey[0].lower() + keySwitchFunctionKey[1:]
                # Make value
                keySwitchFunctionValue = 'Get' \
                    + ''.join([element[0].upper() + element[1:].lower() \
                    for element in fileNameElements])
                # Make Dictionary
                keySwitchFunctionsByPerformanceType[keySwitchFunctionKey] = \
                    globals()[keySwitchFunctionValue]
            
                
                '''with open(filePath + '/' + file, 'rb') as keySwitchFunction: 
                    keySwitchFunctions.append(keySwitchFunction.readlines())
    

    # Make file output
    with open('test.py') as outputFile:
        ''.join(keySwitchFunctions)
        outputFile.write(keySwitchFunctions)'''


print generateKeySwitchFunctions()
