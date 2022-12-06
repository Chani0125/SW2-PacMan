from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from player import PacMan
from enemy import Ghost


class PacManGame(QWidget):
    # 0: 벽, 1: 빈 곳, 2: 쿠키, 3: 파워 쿠키, 4: 팩맨, 5 + n: 유령 + 번호
    map_obj_info = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 5, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 1, 2, 1, 1, 0, 7, 6, 8, 0, 1, 1, 2, 1, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0],
        [0, 3, 2, 0, 2, 2, 2, 2, 2, 4, 2, 2, 2, 2, 2, 0, 2, 3, 0],
        [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    map_img_info = [
        [(3, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (4, 1), (2, 0), (2, 0), (2, 0), (2, 0),
         (2, 0), (2, 0), (2, 0), (2, 0), (3, 1)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (1, 2), (1, 0), (0, 0), (1, 2), (2, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 2), (2, 0), (1, 0),
         (0, 0), (1, 2), (1, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (1, 2), (1, 0), (0, 0), (1, 3), (0, 0), (1, 2), (2, 0), (4, 1), (2, 0), (1, 0), (0, 0), (1, 3),
         (0, 0), (1, 2), (1, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(3, 3), (2, 0), (2, 0), (3, 1), (0, 0), (4, 0), (2, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 2), (2, 0), (4, 2),
         (0, 0), (3, 0), (2, 0), (2, 0), (3, 2)],
        [(0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1),
         (0, 0), (2, 1), (0, 0), (0, 0), (0, 0)],
        [(1, 2), (2, 0), (2, 0), (3, 2), (0, 0), (1, 1), (0, 0), (8, 0), (7, 0), (6, 0), (7, 2), (8, 1), (0, 0), (1, 1),
         (0, 0), (3, 3), (2, 0), (2, 0), (1, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
        [(1, 2), (2, 0), (2, 0), (3, 1), (0, 0), (1, 3), (0, 0), (8, 3), (2, 0), (2, 0), (2, 0), (8, 2), (0, 0), (1, 3),
         (0, 0), (3, 0), (2, 0), (2, 0), (1, 0)],
        [(0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1),
         (0, 0), (2, 1), (0, 0), (0, 0), (0, 0)],
        [(3, 0), (2, 0), (2, 0), (3, 2), (0, 0), (1, 1), (0, 0), (1, 2), (2, 0), (4, 1), (2, 0), (1, 0), (0, 0), (1, 1),
         (0, 0), (3, 3), (2, 0), (2, 0), (3, 1)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (1, 2), (3, 1), (0, 0), (1, 2), (2, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 2), (2, 0), (1, 0),
         (0, 0), (3, 0), (1, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (2, 1), (0, 0), (0, 0), (2, 1)],
        [(4, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 3), (0, 0), (1, 2), (2, 0), (4, 1), (2, 0), (1, 0), (0, 0), (1, 3),
         (0, 0), (1, 1), (0, 0), (1, 2), (4, 2)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (1, 2), (2, 0), (2, 0), (4, 3), (2, 0), (1, 0), (0, 0), (1, 1), (0, 0), (1, 2), (2, 0), (4, 3),
         (2, 0), (2, 0), (1, 0), (0, 0), (2, 1)],
        [(2, 1), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (2, 1)],
        [(3, 3), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0), (2, 0),
         (2, 0), (2, 0), (2, 0), (2, 0), (3, 2)]
    ]

    DISPLAY_SIZE = 2

    def __init__(self):
        super().__init__()
        self.setMapImage()
        self.pacman = PacMan()
        self.ghost = [Ghost(1, 0), Ghost(2, 0), Ghost(3, 0), Ghost(3, 0)]

        self.speed = 100  # 단위 속력 (ms)
        self.timer = QTimer(self)
        self.timer.start(self.speed)
        self.timer.timeout.connect(self.intervalEvent)

    def intervalEvent(self):
        self.pacman.changeShape()
        for ghost in self.ghost:
            ghost.changeShape()
        self.displaytMap()

    def setMapImage(self):
        self.map_img_layout = QGridLayout()
        self.map_img_label = [list() for _ in range(len(self.map_img_info))]
        self.map_img = [list() for _ in range(len(self.map_img_info))]
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                # Make Label For Image
                self.map_img_label[x].append(QLabel())
                self.map_img_label[x][y].resize(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                # Load, Resize, and Rotate Image
                info = self.map_obj_info[x][y]
                if info < 2:
                    file = "images/Map" + str(self.map_img_info[x][y][0]) + ".png"
                elif info == 2:
                    file = "images/Cookie.png"
                elif info == 3:
                    file = "images/PowerCookie.png"
                elif info == 4:
                    file = "images/PacMan1.png"
                elif info == 5:
                    file = "images/Ghost0Left0.png"
                elif info == 6:
                    file = "images/Ghost1Up0.png"
                elif info == 7:
                    file = "images/Ghost2Down0.png"
                elif info == 8:
                    file = "images/Ghost3Down0.png"
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))
                self.map_img[x].append(img)
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])
                self.map_img_layout.addWidget(self.map_img_label[x][y], x, y)
        # Trim White Spaces
        self.map_img_layout.setContentsMargins(0, 0, 0, 0)
        self.map_img_layout.setSpacing(0)
        self.setLayout(self.map_img_layout)

    def displaytMap(self):
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                # Load, Resize, and Rotate Image
                info = self.map_obj_info[x][y]
                if info < 2:
                    file = "images/Map" + str(self.map_img_info[x][y][0]) + ".png"
                elif info == 2:
                    file = "images/Cookie.png"
                elif info == 3:
                    file = "images/PowerCookie.png"
                elif info == 4:
                    file = "images/PacMan" + str(self.pacman.getShape()) + ".png"
                else:
                    ghost_idx = self.map_obj_info[x][y] - 5
                    file = "images/Ghost" + str(ghost_idx) + self.ghost[ghost_idx].getDirect() + str(self.ghost[ghost_idx].getShape()) + ".png"
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))
                self.map_img[x][y] = img
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    game = PacManGame()
    # for i in game.map_img_info:
    #     print("[", end="")
    #     for a, b in i:
    #         print("(\"" + str(a) + "\", " + str(b) + ")", end=", ")
    #     print("]", end="\n")
    # print()
    game.show()
    sys.exit(app.exec_())
