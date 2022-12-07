from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from player import PacMan
from enemy import Ghost

import traceback

class PacManGame(QWidget):
    # 0: 벽, 1: 빈 곳, 2: 쿠키, 3: 파워 쿠키
    map_init_obj_info = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0],
        [0, 3, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 3, 0],
        [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # 0: 벽, 1: 빈 곳, 2: 쿠키, 3: 파워 쿠키
    map_obj_info = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 3, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 3, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 2, 0, 0, 0, 1, 0, 1, 0, 0, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 1, 2, 1, 1, 0, 1, 1, 1, 0, 1, 1, 2, 1, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [1, 1, 1, 0, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 1, 1, 1],
        [0, 0, 0, 0, 2, 0, 1, 0, 0, 0, 0, 0, 1, 0, 2, 0, 0, 0, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 2, 0, 0, 0, 2, 0, 2, 0, 0, 0, 2, 0, 0, 2, 0],
        [0, 3, 2, 0, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 3, 0],
        [0, 0, 2, 0, 2, 0, 2, 0, 0, 0, 0, 0, 2, 0, 2, 0, 2, 0, 0],
        [0, 2, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 0, 2, 2, 2, 2, 0],
        [0, 2, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # 0: 길, 1: 교차로
    map_int_info = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    map_int_direct_info = [
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 1, 1, 0), (0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 1, 1), (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0),
         (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 1, 1, 1), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0), (0, 0, 0, 0), (0, 1, 1, 1), (0, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0),
         (0, 1, 1, 0), (0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0), (1, 0, 1, 1), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0),
         (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(1, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0), (0, 1, 1, 1), (0, 0, 0, 0),
         (1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (1, 0, 1, 1), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 0, 1, 1), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 1, 1, 1), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (1, 0, 0, 0), (0, 0, 0, 0), (0, 1, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0),
         (0, 1, 1, 0), (0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 1, 1, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 0, 1), (0, 1, 1, 0), (0, 0, 0, 0), (1, 0, 1, 1), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0),
         (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 1, 0), (0, 0, 0, 0), (0, 1, 1, 1), (0, 0, 0, 0),
         (1, 0, 1, 0), (0, 1, 0, 1), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 1, 0), (1, 1, 0, 1), (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0),
         (0, 1, 1, 0), (0, 0, 0, 0), (1, 0, 1, 0), (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0),
         (1, 1, 0, 1), (0, 1, 1, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (1, 0, 0, 1), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (1, 1, 0, 1), (0, 0, 0, 0), (1, 1, 0, 1), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 1, 0, 1), (0, 0, 0, 0)],
        [(0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0),
         (0, 0, 0, 0), (0, 0, 0, 0), (0, 0, 0, 0)]
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
        [(2, 0), (2, 0), (2, 0), (3, 2), (0, 0), (1, 1), (0, 0), (8, 0), (7, 0), (6, 0), (7, 2), (8, 1), (0, 0), (1, 1),
         (0, 0), (3, 3), (2, 0), (2, 0), (2, 0)],
        [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0), (0, 0), (2, 1), (0, 0), (0, 0),
         (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)],
        [(2, 0), (2, 0), (2, 0), (3, 1), (0, 0), (1, 3), (0, 0), (8, 3), (2, 0), (2, 0), (2, 0), (8, 2), (0, 0), (1, 3),
         (0, 0), (3, 0), (2, 0), (2, 0), (2, 0)],
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

    PACMANINTERVAL = 5

    GHOSTINTERVAL = 4


    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 3
        self.num_cookie = 150
        self.setMapImage()
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]
        self.gameTime = 0
        self.die = False

        self.interval = 100  # 단위 속력 (ms)
        self.timer = QTimer(self)
        self.timer.start(self.interval)
        self.timer.timeout.connect(self.intervalEvent)

    def resetGame(self):
        self.life -= 1
        self.resetMapImage()
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]

    def intervalEvent(self):
        try:
            print(self.score)
            self.gameTime += 1
            # Display
            if self.die:
                if self.pacman.getShape() < 4:
                    self.pacman.changeShape(self.pacman.getShape()+1)
                else:
                    self.resetGame()
            else:
                self.pacman.changeShape()
                for ghost in self.ghost:
                    ghost.changeShape()
            self.displaytMap()
            self.displayEntities()
            if self.die:
                return
            # Check Touch
            for ghost in self.ghost:
                if self.pacman.getLocation() == ghost.getLocation():
                    self.die = True
                    return
            # PacMan Move
            fore_pacman_x, fore_pacman_y = self.pacman.getForeLocation()
            if self.map_obj_info[fore_pacman_x][fore_pacman_y] == 0:
                self.pacman.setShapeChange(False)
            else:
                self.pacman.setShapeChange(True)
                if self.gameTime % self.PACMANINTERVAL == 0:
                    self.pacman.move()
            # Ghost Move
            for ghost in self.ghost:
                if ghost.isActive():
                    if self.gameTime % self.GHOSTINTERVAL == 0:
                        ghost_x, ghost_y = ghost.getLocation()
                        fore_ghost_x, fore_ghost_y = ghost.getForeLocation()
                        if self.map_int_info[ghost_x][ghost_y] == 1 or self.map_obj_info[fore_ghost_x][fore_ghost_y] == 0:
                            d = self.map_int_direct_info[ghost_x][ghost_y]
                            if self.map_int_info[ghost_x][ghost_y] == 0:
                                for i in range(len(d)):
                                    if d[i] == 1 and ghost.getOppositeDirect() != i:
                                        ghost.setDirect(i)
                                        break
                            else:
                                direct_bnum = 0
                                for i in range(len(d)):
                                    if d[i] == 1 and ghost.getOppositeDirect() != i:
                                        direct_bnum += 2 ** i
                                ghost.changeDirect(direct_bnum)
                        ghost.move()
            # Eat Cookie and Power Cookie
            pacman_x, pacman_y = self.pacman.getLocation()
            if self.map_obj_info[pacman_x][pacman_y] == 2:
                self.score += 10
                self.num_cookie -= 1
                self.map_obj_info[pacman_x][pacman_y] = 1
            elif self.map_obj_info[pacman_x][pacman_y] == 3:
                self.score += 50
                self.num_cookie -= 1
                self.map_obj_info[pacman_x][pacman_y] = 1
            # Spawn Rest Ghosts
            if self.gameTime == 50 - self.GHOSTINTERVAL:
                self.ghost[1].setLocation(8, 9)
                self.ghost[1].setDirect(3)
            if self.gameTime == 50:
                self.ghost[1].setLocation(7, 9)
            if self.gameTime == 50 + self.GHOSTINTERVAL:
                self.ghost[1].setActive(True)
                self.ghost[1].changeDirect(3)
                self.ghost[1].move()
            if self.gameTime == 100 - self.GHOSTINTERVAL * 2:
                self.ghost[2].setLocation(9, 9)
                self.ghost[2].setDirect(0)
            if self.gameTime == 100 - self.GHOSTINTERVAL:
                self.ghost[2].setLocation(8, 9)
                self.ghost[2].setDirect(3)
            if self.gameTime == 100:
                self.ghost[2].setLocation(7, 9)
            if self.gameTime == 100 + self.GHOSTINTERVAL:
                self.ghost[2].setActive(True)
                self.ghost[2].changeDirect(3)
                self.ghost[2].move()
            if self.gameTime == 150 - self.GHOSTINTERVAL * 2:
                self.ghost[3].setLocation(9, 9)
                self.ghost[3].setDirect(1)
            if self.gameTime == 150 - self.GHOSTINTERVAL:
                self.ghost[3].setLocation(8, 9)
                self.ghost[3].setDirect(3)
            if self.gameTime == 150:
                self.ghost[3].setLocation(7, 9)
            if self.gameTime == 150 + self.GHOSTINTERVAL:
                self.ghost[3].setActive(True)
                self.ghost[3].changeDirect(3)
                self.ghost[3].move()
        except:
            print(traceback.format_exc())

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
                if x == 15 and y == 9:
                    file = "images/PacMan1.png"
                elif x == 7 and y == 9:
                    file = "images/Ghost0Left0.png"
                elif x == 9 and y == 9:
                    file = "images/Ghost1Up0.png"
                elif x == 9 and y == 8:
                    file = "images/Ghost2Down0.png"
                elif x == 9 and y == 10:
                    file = "images/Ghost3Down0.png"
                elif info < 2:
                    file = "images/Map" + str(self.map_img_info[x][y][0]) + ".png"
                elif info == 2:
                    file = "images/Cookie.png"
                elif info == 3:
                    file = "images/PowerCookie.png"
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))
                self.map_img[x].append(img)
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])
                self.map_img_layout.addWidget(self.map_img_label[x][y], x, y)
        # Trim White Spaces
        self.map_img_layout.setContentsMargins(0, 0, 0, 0)
        self.map_img_layout.setSpacing(0)
        self.setLayout(self.map_img_layout)

    def resetMapImage(self):
        self.gameTime = 0
        self.die = False
        for ghost in self.ghost:
            ghost.setActive(True)
        self.pacman.setShapeChange(True)
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                # Load, Resize, and Rotate Image
                info = self.map_obj_info[x][y]
                if x == 15 and y == 9:
                    file = "images/PacMan1.png"
                elif x == 7 and y == 9:
                    file = "images/Ghost0Left0.png"
                elif x == 9 and y == 9:
                    file = "images/Ghost1Up0.png"
                elif x == 9 and y == 8:
                    file = "images/Ghost2Down0.png"
                elif x == 9 and y == 10:
                    file = "images/Ghost3Down0.png"
                elif info < 2:
                    file = "images/Map" + str(self.map_img_info[x][y][0]) + ".png"
                elif info == 2:
                    file = "images/Cookie.png"
                elif info == 3:
                    file = "images/PowerCookie.png"
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))
                self.map_img[x].append(img)
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])

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

    def displayEntities(self):
        # Display Ghost
        for i in range(len(self.ghost)):
            x, y = self.ghost[i].getLocation()
            file = "images/Ghost" + str(i) + self.ghost[i].getDirect() + str(self.ghost[i].getShape()) + ".png"
            img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            self.map_img[x][y] = img
            self.map_img_label[x][y].setPixmap(self.map_img[x][y])
        # Display PacMan
        x, y = self.pacman.getLocation()
        file = "images/PacMan" + str(self.pacman.getShape()) + ".png"
        img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
        img = img.transformed(QTransform().rotate(self.pacman.getDirect() * 90))
        self.map_img[x][y] = img
        self.map_img_label[x][y].setPixmap(self.map_img[x][y])

    def keyPressEvent(self, key_event):
        if key_event.key() == Qt.Key_Right:
            self.pacman.setDirect(0)
        elif key_event.key() == Qt.Key_Left:
            self.pacman.setDirect(1)
        elif key_event.key() == Qt.Key_Down:
            self.pacman.setDirect(2)
        elif key_event.key() == Qt.Key_Up:
            self.pacman.setDirect(3)


if __name__ == '__main__':
    import sys

    try:
        app = QApplication(sys.argv)
        game = PacManGame()
        game.show()
        sys.exit(app.exec_())
    except:
        print(traceback.format_exc())
