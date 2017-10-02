import csv

import sfz_region

def ParseCsv(filename):
    with open(filename, 'rb') as csvFile:
        data = csv.reader(csvFile)
        rowIndex = 0
        sfzRegions = []
        for row in data:
            try:
                sfzRegions.append(sfz_region.SfzRegion(row))
            except sfz_region.CsvParseError:
                print 'Found Error in {}:{}'.format(filename, rowIndex + 1)
                raise
            else:
                rowIndex += 1

    return sfz_region.SfzRegions(sfzRegions)
