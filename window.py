import cv2 as cv
import numpy as np
class Window:
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
    #def createTrackbar(self,label,group)
    def showWindow(self):
        cv.imshow(self.name,self.image)