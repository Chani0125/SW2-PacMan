class Ghost:

    def __init__(self, direct, shape):
        self.direct = direct
        self.shape = shape
        self.shapeChange = True

    def changeShape(self):
        if self.shapeChange:
            self.shape = 1 - self.shape

    def setDirect(self, direct):
        self.direct = direct

    def getShape(self):
        return self.shape

    def getDirect(self):
        if self.direct == 0:
            return "Right"
        elif self.direct == 1:
            return "Left"
        elif self.direct == 2:
            return "Down"
        else:
            return "Up"
