import cv2 as cv
import numpy as np
import file
import window
def readCV():
    cvFile=file.File('eeg_flex_007_Desconocido.csv')
    cvFile.readAndSaveData()
def sampleDrawingsInWindows():
    W = 400
    windowInstance=window.Window('classed based window',(W, W, 3))
    windowInstance2=window.Window('classed based window2',(W, W, 3))
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