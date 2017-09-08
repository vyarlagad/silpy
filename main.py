from pytest import *
from MIG import *
import numpy as np
from ImageViewer import *

image = MIG(8,8, np.matrix([
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
    [0,1,2,3,4,255,6,7],
]))

imageImport = readMIGFile('./res/lena_sm.mig')
#print imageImport.matrix

viewer = ImageViewer()

viewer.loadMIG(imageImport)

#image.save('./res/testImage.mig')
