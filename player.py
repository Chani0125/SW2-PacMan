class PacMan:

    def __init__(self):
        self.shape = 1
        self.increase = False
        self.shapeChange = True

    def changeShape(self, idx=-1):
        if idx < 0:
            if self.shapeChange:
                if self.increase:
                    self.shape += 1
                    if self.shape == 2:
                        self.increase = False
                else:
                    self.shape -= 1
                    if self.shape == 0:
                        self.increase = True
        elif idx < 5:
            self.shape = idx
        else:
            print("Error: PacMac Shape Index Error")

    def getShape(self):
        return self.shape
