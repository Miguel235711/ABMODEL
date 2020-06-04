import csv

class File:
    
    #location of file
    fileLocation=None
    #[[],[],...], matrix with data
    dataRows=None
    #amount of hat sensors
    amountOfSensors=None
    #amount of waves 
    amountOfWaves=4

    def __init__(self,fileLocation):
        self.fileLocation=fileLocation
    
    def readAndSaveData(self):
        with open(self.fileLocation,'r') as fileL:
            reader = csv.reader(fileL)
            self.dataRows=list(reader)
            print 'data read and saved correctly'
            #print 'number of rows:',len(self.dataRows)
            print 'elements per rows:',len(self.dataRows[0])
            self.amountOfSensors=(len(self.dataRows[0])-1)/self.amountOfWaves
    
    def getAverageOfWavesAndTime(self,row):
        if row >= len(self.dataRows):#invalid row
            return None
        ans=[0]*self.amountOfWaves
        for i in xrange(1,len(self.dataRows[row])-1):
            ans[(i-1)%self.amountOfWaves]+=float(self.dataRows[row][i])
        for i in xrange(0,self.amountOfWaves):
            ans[i]/=self.amountOfSensors
        return (float(self.dataRows[row][0]),ans)
    
    def getAllData(self):
        return [self.getAverageOfWavesAndTime(i) for i in xrange(len(self.dataRows))]

    
            