import csv
import xlrd
import numbers
from openpyxl import load_workbook

class File:
    
    #location of file
    fileLocation=None
    #[[],[],...], matrix with data
    dataRows=None
    #amount of hat sensors
    amountOfSensors=None
    #amount of waves 
    amountOfWaves=4
    __maxVal=10

    def __init__(self,fileLocation):
        self.fileLocation=fileLocation
    def __calcAmountOfSensors(self):
        self.amountOfSensors=(len(self.dataRows[0])-1)/self.amountOfWaves  
    def readAndSaveData(self): 
        #returns True if is gamma in place of delta, 
        # otherwise it returns False
        ##print('filelocation {}'.format(self.fileLocation))
        fileFormat = self.fileLocation.split('.').pop()
        ##print('fileformat: {}'.format(fileFormat))
        #read data table
        if fileFormat == 'csv':
            #fill dataRows[][] from .csv
            with open(self.fileLocation,'r') as fileL:
                reader = csv.reader(fileL)
                self.dataRows=list(reader)
                ##print('dataRows: ${}'.format(self.dataRows))
                ##print 'data read and saved correctly'
                ##print 'number of rows:',len(self.dataRows)
                ##print 'elements per rows:',len(self.dataRows[0])
        elif fileFormat == 'xls':
            #fill dataRows[][] from xlsx
            sheet = xlrd.open_workbook(self.fileLocation).sheet_by_index(0)
            ##print('sheet rows: {}'.format(sheet.nrows))
            self.dataRows = [sheet.row_values(i) for i in range(sheet.nrows)]
            ##print('dataRows from xlsx {}'.format(self.dataRows))
            #for i in range(sheet.nrows):
            #    #print('row {} {}'.format(i,sheet.row_values(i)))
            ##print('dataRows from xlsx {}'.format(self.dataRows))
        elif fileFormat == 'xlsx':
            ##print('elif fileFormat == xlsx is true')
            ws = load_workbook(filename = self.fileLocation).active
            ##print(ws.values)
            self.dataRows = [ [cell for cell in row  ] for row in ws.values ]
            ##print('xlsx self.dataRows: {}'.format(self.dataRows))
        #save copy for ad-hoc file configurations
        dataRowsCopy = self.dataRows
        #remove non number rows
        self.dataRows = [ row for row in self.dataRows if self.__parseToFloat(row[0])!=0.0 or self.__parseToFloat(row[1])!=0.0] #super specific way of removing it
        ##print('self.dataRows = {}'.format(self.dataRows))
        #*check ad-hoc file configurations (using dataRowsCopy): 
        #  1. if "gamma" (case insensitive) pattern is found in any part
        #     of the input, change dinamically in multiGraphContainer.py "delta" by "gamma"
        #  2. if "betaL" and "betaR" patterns are found in any part of the
        #     of the input, reduce "betaL" and "betaH" columns to single "beta" 
        #     column through average function 
        gammaFound,betaLHFoundPos,LPos = False,{},None
        #betaLHFoundPos has H as key and L as value
        for i,row in enumerate(dataRowsCopy):
            for j,cell in enumerate(row):
                if type(cell) == str:
                    cellLower = cell.lower()
                    gammaFound |= cellLower.find('gamma') != -1
                    betaLPos = cellLower.find('betal')
                    if betaLPos != -1:
                        LPos = j
                    betaHPos = cellLower.find('betah') 
                    if betaHPos != -1:
                        betaLHFoundPos[j]=LPos
        ##print('gammaFound: {}'.format(gammaFound))
        #timestamp normalization definition
        self.dataRows[0][0] = self.__parseToFloat(self.dataRows[0][0])
        firstTimeNorm = self.dataRows[0][0] if self.dataRows[0][0] > 1000 else 0.0 
        for i in range(len(self.dataRows)):
            for j in range(len(self.dataRows[i])):
                self.dataRows[i][j] = self.__parseToFloat(self.dataRows[i][j])
                #check if going to make beta reduction
                if j in betaLHFoundPos:
                    #make beta reduction
                    betaLPos = betaLHFoundPos[j]
                    self.dataRows[i][betaLPos] += self.dataRows[i][j]
                    self.dataRows[i][betaLPos]/=2
             #timestamp normalization
            self.dataRows[i][0] = self.dataRows[i][0] - firstTimeNorm
        #remove extra betaH for the case of beta reduction
        self.dataRows = [ [ cell for j,cell in enumerate(row) if j not in betaLHFoundPos ] for row in self.dataRows ]
        ##print(len(self.dataRows[0]))
        ##print('dataRows {}'.format(self.dataRows))
        #reduce beta if betaLFoundPos and betaHFoundPos are not empty
        self.__calcAmountOfSensors()
        return gammaFound
              
    def getAverageOfWavesAndTime(self,row):
        if row >= len(self.dataRows):#invalid row
            return None
        ans=[0.0]*self.amountOfWaves
        for i in range(1,len(self.dataRows[row])-1):
            ans[(i-1)%self.amountOfWaves]+=self.dataRows[row][i]
        for i in range(0,self.amountOfWaves):
            ans[i]/=self.amountOfSensors
        return (self.dataRows[row][0],ans)
    
    def getAverageData(self):
        return [self.getAverageOfWavesAndTime(i) for i in range(len(self.dataRows))]
    def __parseToFloat(self, x): 
        try:
            return float(x)
        except:
            return 0.0
    def __getNormalizedWaveValuesPerNode(self,i):
        return [ (self.dataRows[row][0],[max(0,min(self.dataRows[row][col]/self.__maxVal,self.__maxVal)) for col in range(i+1,len(self.dataRows[row]),4)]) for row in range(len(self.dataRows))]
    def getNormalizedNodeData(self):
        return [self.__getNormalizedWaveValuesPerNode(i) for i in range(self.amountOfWaves)]
    
            