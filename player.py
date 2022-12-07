class PacMan:

    def __init__(self):
        self.direct = 1
        self.shape = 1
        self.increase = False
        self.shapeChange = True
        self.x = 15
        self.y = 9

    def changeShape(self, idx=-1):
        if idx < 0:
            if self.shapeChange or not self.shape == 1:
                if self.increase:
                    self.shape += 1
                    if self.shape == 2:
                        self.increase = False
                else:
                    self.shape -= 1
                    if self.shape == 0:
                        self.increase = True
        elif idx < 6:
            self.shape = idx
        else:
            print("Error: PacMac Shape Index Error")

    def setShapeChange(self, shapeChange):
        self.shapeChange = shapeChange

    def getShape(self):
        return self.shape

    def getLocation(self):
        return self.x % 21, self.y % 19

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        if self.direct == 0:
            self.y += 1
        elif self.direct == 1:
            self.y -= 1
        elif self.direct == 2:
            self.x += 1
        else:
            self.x -= 1

    def getForeLocation(self):
        if self.direct == 0:
            return self.x % 21, (self.y + 1) % 19
        elif self.direct == 1:
            return self.x % 21, (self.y - 1) % 19
        elif self.direct == 2:
            return (self.x + 1) % 21, self.y % 19
        else:
            return (self.x - 1) % 21, self.y % 19

    def setDirect(self, direct):
        self.direct = direct

    def getDirect(self):
        if self.direct == 0:
            return 2
        elif self.direct == 1:
            return 0
        elif self.direct == 2:
            return 3
        else:
            return 1