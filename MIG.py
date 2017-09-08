import numpy as np

class MIG:
    def __init__(self, path):
        with open(self.path, 'rb') as f:
            self.width = f.read(1)
            self.height = f.read(1)
            image_data = [[[None] for j in range(self.width)] for i in range(self.height)]
            for i in range(self.height):
                for j in range(self.width):
                    self.matrix[i][j] = f.read(1)
            self.matrix = np.matrix(image_data)

    def __init__(self, width=0, height=0, matrix=np.matrix([])):
        self.width = width
        self.height = height
        self.matrix = matrix

    def getHeight(self):
        return self.height

    def getWidth(self):
        return self.width

    def getIntensity(self, x, y):
        return self.matrix.tolist()[y][x]

    def toMatrix(self):
        return self.matrix

    def save(self, path):
        image_data = [self.getWidth(), self.getHeight()]
        for row in self.matrix.tolist():
            for cell in row:
                image_data.append(cell)
        image_bytes = bytearray(image_data)
        with open(path, 'wb') as f:
            f.write(image_bytes)

def readMIGFile(path):
    def byteToInt(byte):
        return int(byte.encode('hex'), 16)

    with open(path, 'rb') as f:
        width = byteToInt(f.read(1))
        height = byteToInt(f.read(1))
        print "hello!"
        print '\"'+str(width)+'\"'
        image_data = [[[None] for j in range(width)] for i in range(height)]
        for i in range(height):
            for j in range(width):
                image_data[i][j] = byteToInt(f.read(1))
        matrix = np.matrix(image_data)
        return MIG(width, height, matrix)
