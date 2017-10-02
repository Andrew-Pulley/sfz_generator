import parse_csv

def CsvToSfz(csvFileName):
    sfzRegions = parse_csv.ParseCsv(csvFileName)
    
    # Now do something with sfzRegions...
    

if __name__ == '__main__':
    import sys
    CsvToSfz(sys.argv[1])
