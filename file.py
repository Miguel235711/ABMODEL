import csv
class File:
    #location of file
    fileLocation=None
    #[[],[],...], matrix with data
    dataRows=None
    def __init__(self,fileLocation):
        self.fileLocation=fileLocation
    def readAndSaveData(self):
        with open(self.fileLocation,'r') as fileL:
            reader = csv.reader(fileL)
            self.dataRows=list(reader)
            print 'data read and saved correctly'
            print 'number of rows:',len(self.dataRows)
            print 'elements per rows:',len(self.dataRows[0])