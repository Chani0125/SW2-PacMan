class Ghost:

    def __init__(self, direct, shape, x, y):
        self.direct = direct
        self.shape = shape
        self.shapeChange = True
        self.x = x
        self.y = y

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

    def getLocation(self):
        return self.x, self.y

    # def move(self):
    #     self.direct =
    #
    # def changeDirect(self, *direct):
