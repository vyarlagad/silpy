from graphics import *

class ImageViewer:
    def __init__(self, title="Image Viewer"):
        self.title = title

    def loadMIG(self, mig):
        win = GraphWin(self.title, mig.getWidth(), mig.getHeight())
        for y in range(mig.getHeight()):
            for x in range(mig.getWidth()):
                intensity = mig.getIntensity(x,y)
                win.plotPixel(x,y,color_rgb(intensity, intensity, intensity))
        win.getMouse() # pause for click in window
        win.close()
