import cv2 as cv
import numpy as np
import csv
class file:
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
class window:
    #name of window
    name=None
    #size of window
    size=None
    #window content
    image=None
    def __init__(self,name,size):
        #black empty image creation
        self.image=np.zeros(size, dtype=np.uint8)
        self.name=name
        self.size=size
    def drawEllipse(self,center,axes,angle,color,thickness,line_type):
        cv.ellipse(self.image,
                center,
                axes,
                angle,
                0,
                360,
                color,
                thickness,
                line_type)
    def drawCircle(self,center,radius,color,thickness,line_type):
        cv.circle(self.image,
               center,
               radius,
               color,
               thickness,
               line_type)
    def drawRectangle(self,pt1,pt2,color,thickness,line_type):
        cv.rectangle(self.image,
                pt1,
                pt2,
                color,
                thickness,
                line_type
        )
    def drawLine(self,start,end,color,thickness,line_type):
        cv.line(self.image,
             start,
             end,
             color,
             thickness,
             line_type)
    def drawConvexPolygon(self,matrix,line_type):
        ppt=np.array(matrix,np.int32)
        ppt = ppt.reshape((-1, 1, 2))
        cv.fillPoly(self.image, [ppt], (255, 255, 255), line_type)
    def showWindow(self):
        cv.imshow(self.name,self.image)
def readCV():
    cvFile=file('eeg_flex_007_Desconocido.csv')
    cvFile.readAndSaveData()
def sampleDrawingsInWindows():
    W = 400
    windowInstance=window('classed based window',(W, W, 3))
    windowInstance2=window('classed based window2',(W, W, 3))
    windowInstance.drawEllipse(
        (W // 2, W // 2),
        (W // 4, W // 16),
        90,
        (255, 0, 0),
        2,
        8
    )
    windowInstance.drawEllipse(
        (W // 2, W // 2),
        (W // 4, W // 16),
        45,
        (255, 0, 0),
        2,
        8
    )
    windowInstance.drawEllipse(
        (W // 2, W // 2),
        (W // 4, W // 16),
        -45,
        (255, 0, 0),
        2,
        8
    )
    windowInstance.drawEllipse(
        (W // 2, W // 2),
        (W // 4, W // 16),
        0,
        (255, 0, 0),
        2,
        8
    )
    windowInstance.drawCircle(
        (W // 2, W // 2),
        W // 32,
        (0, 0, 255),
        -1,
        8
    )
    windowInstance.drawRectangle(
        (0, 7 * W // 8),
        (W, W),
        (0, 255, 255),
        -1,
        8
    )
    windowInstance.drawLine((0, 15 * W // 16), (W, 15 * W // 16),(0,0,0),2,8)
    windowInstance.drawLine((W // 4, 7 * W // 8), (W // 4, W),(0,0,0),2,8)
    windowInstance.drawLine((W // 2, 7 * W // 8), (W // 2, W),(0,0,0),2,8)
    windowInstance.drawLine((3 * W // 4, 7 * W // 8), (3 * W // 4, W),(0,0,0),2,8)
    windowInstance2.drawConvexPolygon(
        [
         [W / 4, 7 * W / 8], [3 * W / 4, 7 * W / 8],
         [3 * W / 4, 13 * W / 16], [11 * W / 16, 13 * W / 16],
         [19 * W / 32, 3 * W / 8], [3 * W / 4, 3 * W / 8],
         [3 * W / 4, W / 8], [26 * W / 40, W / 8],
         [26 * W / 40, W / 4], [22 * W / 40, W / 4],
         [22 * W / 40, W / 8], [18 * W / 40, W / 8],
         [18 * W / 40, W / 4], [14 * W / 40, W / 4],
         [14 * W / 40, W / 8], [W / 4, W / 8],
         [W / 4, 3 * W / 8], [13 * W / 32, 3 * W / 8],
         [5 * W / 16, 13 * W / 16], [W / 4, 13 * W / 16]
        ],
        8
    )
    windowInstance.showWindow()
    windowInstance2.showWindow()
    cv.waitKey(0)
    cv.destroyAllWindows()
def main():
    readCV()
    sampleDrawingsInWindows() 
main()