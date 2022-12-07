import random


class Ghost:

    def __init__(self, direct, shape, x, y, active):
        # 유령의 모양과 관련된 변수
        self.direct = direct  # 이동과 관련
        self.shape = shape
        self.shapeChange = True
        self.powerCookie = False
        self.active = active
        # 유령의 위치
        self.x = x
        self.y = y

    def isActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

    def isPowerCookie(self):
        return self.powerCookie

    def setPowerCookie(self, powerCookie):
        self.powerCookie = powerCookie

    def changeShape(self):
        if self.shapeChange:
            self.shape = 1 - self.shape

    def setDirect(self, direct):
        self.direct = direct

    def getShape(self):
        return self.shape

    # 이미지 파일을 불러오기 위해 문자 방향 출력
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
        # IndexError를 방지하기 위해 % 사용
        return self.x % 21, self.y % 19

    def setLocation(self, x, y):
        self.x = x
        self.y = y

    def getForeLocation(self):
        # IndexError를 방지하기 위해 % 사용
        if self.direct == 0:
            return self.x % 21, (self.y + 1) % 19
        elif self.direct == 1:
            return self.x % 21, (self.y - 1) % 19
        elif self.direct == 2:
            return (self.x + 1) % 21, self.y % 19
        else:
            return (self.x - 1) % 21, self.y % 19

    def move(self):
        if self.direct == 0:
            self.y += 1
        elif self.direct == 1:
            self.y -= 1
        elif self.direct == 2:
            self.x += 1
        else:
            self.x -= 1

    def changeDirect(self, direct_bnum):
        # 임의로 유령 방향 설정
        # 방향에 대한 이진수를 리스트로 재구성
        direct = []
        for i in range(4):
            if (direct_bnum >> i) % 2 == 1:
                direct.append(i)
        else:
            self.direct = random.choice(direct)

    def getOppositeDirect(self):
        # 유령이 바라보고 있는 반대 방향 출력
        if self.direct == 0:
            return 1
        elif self.direct == 1:
            return 0
        elif self.direct == 2:
            return 3
        else:
            return 2
