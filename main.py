from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtTest import *

from player import PacMan
from enemy import Ghost

import traceback
import winsound
import sys


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

    INTERVAL = 50

    DISPLAY_SIZE = 2

    PACMAN_INTERVAL = 6

    GHOST_INTERVAL = 5

    GHOST_SPAWN_INTERVAL = 125

    DEATH_INTERVAL = 3

    def __init__(self):
        super().__init__()
        # Initial Setting
        self.setWindowTitle('PacMan Game')

        self.score = 0
        self.life = 3
        self.num_cookie = 150
        self.setInitMapImage()
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]
        self.game_time = 0
        self.game_total_time = 0
        self.die = False
        self.over = False
        self.game_over = False

        self.timer = QTimer(self)
        self.timer.start(self.INTERVAL)
        self.timer.timeout.connect(self.intervalEvent)

    def resetGame(self):
        self.resetMapImage()
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]

    def gameOver(self):
        for y in range(7, 12):
            self.map_img_label[11][y].setText("OVER!"[y - 7])
            over_font = self.map_img_label[11][y].font()
            over_font.setPointSize(18)
            if self.over:
                self.map_img_label[11][y].setStyleSheet("color: yellow;"
                                                        "background-color: #000000")
            else:
                self.map_img_label[11][y].setStyleSheet("color: green;"
                                                        "background-color: #000000")
            self.map_img_label[11][y].setFont(over_font)
            self.map_img_label[11][y].setAlignment(Qt.AlignCenter)
        self.game_over = True

    def intervalEvent(self):
        try:
            if self.game_over:
                return
            self.game_total_time += 1
            if self.game_total_time > 3000 // self.INTERVAL:
                self.game_time += 1
                if self.num_cookie == 0:
                    self.gameOver()
                    return
                # Display
                if self.die:
                    if self.game_time % self.DEATH_INTERVAL == 0 and self.game_time >= self.DEATH_INTERVAL * 2:
                        if self.pacman.getShape() < 5:
                            self.pacman.changeShape(self.pacman.getShape() + 1)
                        else:
                            if self.over:
                                self.gameOver()
                                return
                            else:
                                self.resetGame()
                else:
                    self.pacman.changeShape()
                    for ghost in self.ghost:
                        if self.game_time % 2 == 0:
                            ghost.changeShape()
                self.displayMap()
                self.displayEntities()
                if self.die:
                    return
                # Check Touch
                for ghost in self.ghost:
                    if self.pacman.getLocation() == ghost.getLocation():
                        self.die = True
                        self.game_time = 0
                        self.life -= 1
                        winsound.PlaySound("musics/pacman_death.wav", winsound.SND_ASYNC)
                        if self.life == 0:
                            self.over = True
                        return
                # PacMan Move
                fore_pacman_x, fore_pacman_y = self.pacman.getForeLocation()
                if fore_pacman_x == 9 and fore_pacman_y == 19:
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.setLocation(9, 0)
                elif fore_pacman_x == 9 and fore_pacman_y == -1:
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.setLocation(9, 18)
                elif self.map_obj_info[fore_pacman_x][fore_pacman_y] == 0:
                    self.pacman.setShapeChange(False)
                else:
                    self.pacman.setShapeChange(True)
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.move()
                # Ghost Move
                for ghost in self.ghost:
                    if ghost.isActive() and self.game_time % self.GHOST_INTERVAL == 0:
                        ghost_x, ghost_y = ghost.getLocation()
                        fore_ghost_x, fore_ghost_y = ghost.getForeLocation()
                        if fore_ghost_x == 9 and fore_ghost_y == 19:
                            ghost.setLocation(9, 0)
                        elif fore_pacman_x == 9 and fore_ghost_y == -1:
                            ghost.setLocation(9, 18)
                        elif self.map_int_info[ghost_x][ghost_y] == 1 or self.map_obj_info[fore_ghost_x][fore_ghost_y] == 0:
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
                    winsound.PlaySound("musics/pacman_chomp.wav", winsound.SND_ASYNC)
                    self.score += 10
                    self.num_cookie -= 1
                    self.map_obj_info[pacman_x][pacman_y] = 1
                elif self.map_obj_info[pacman_x][pacman_y] == 3:
                    winsound.PlaySound("musics/pacman_chomp.wav", winsound.SND_ASYNC)
                    self.score += 50
                    self.num_cookie -= 1
                    self.map_obj_info[pacman_x][pacman_y] = 1
                # Spawn Rest Ghosts
                if self.game_time == self.GHOST_SPAWN_INTERVAL - self.GHOST_INTERVAL:
                    self.ghost[1].setLocation(8, 9)
                    self.ghost[1].setDirect(3)
                if self.game_time == self.GHOST_SPAWN_INTERVAL:
                    self.ghost[1].setLocation(7, 9)
                if self.game_time == self.GHOST_SPAWN_INTERVAL + self.GHOST_INTERVAL:
                    self.ghost[1].setActive(True)
                    self.ghost[1].changeDirect(3)
                    self.ghost[1].move()
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 2 - self.GHOST_INTERVAL * 2:
                    self.ghost[2].setLocation(9, 9)
                    self.ghost[2].setDirect(0)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 2 - self.GHOST_INTERVAL:
                    self.ghost[2].setLocation(8, 9)
                    self.ghost[2].setDirect(3)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 2:
                    self.ghost[2].setLocation(7, 9)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 2 + self.GHOST_INTERVAL:
                    self.ghost[2].setActive(True)
                    self.ghost[2].changeDirect(3)
                    self.ghost[2].move()
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 3 - self.GHOST_INTERVAL * 2:
                    self.ghost[3].setLocation(9, 9)
                    self.ghost[3].setDirect(1)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 3 - self.GHOST_INTERVAL:
                    self.ghost[3].setLocation(8, 9)
                    self.ghost[3].setDirect(3)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 3:
                    self.ghost[3].setLocation(7, 9)
                if self.game_time == self.GHOST_SPAWN_INTERVAL * 3 + self.GHOST_INTERVAL:
                    self.ghost[3].setActive(True)
                    self.ghost[3].changeDirect(3)
                    self.ghost[3].move()
        except:
            print(traceback.format_exc())

    def setInitMapImage(self):
        self.map_img_layout = QGridLayout()
        # Scoreboard
        self.scoreboard = QLabel(str(self.score))
        self.scoreboard.setStyleSheet("color: white;"
                                      "background-color: #000000")
        self.scoreboard.setMargin(12)
        scoreboard_font = self.scoreboard.font()
        scoreboard_font.setPointSize(12)
        self.scoreboard.setFont(scoreboard_font)
        self.scoreboard.resize(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE * 19)
        self.map_img_layout.addWidget(self.scoreboard, 0, 0, 1, 19)
        # Map
        self.map_img_label = [list() for _ in range(len(self.map_img_info) + 1)]
        self.map_img = [list() for _ in range(len(self.map_img_info) + 1)]
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                if x == 11 and (6 < y < 12):
                    self.map_img_label[x].append(QLabel("READY"[y - 7]))
                    ready_font = self.map_img_label[x][y].font()
                    ready_font.setPointSize(18)
                    self.map_img_label[x][y].setStyleSheet("color: yellow;"
                                                           "background-color: #000000")
                    self.map_img_label[x][y].setFont(ready_font)
                    self.map_img_label[x][y].setAlignment(Qt.AlignCenter)
                    self.map_img[x].append(None)
                else:
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
                self.map_img_layout.addWidget(self.map_img_label[x][y], x + 1, y, 1, 1)
        # PacMan Life
        for y in range(3):
            self.map_img_label[21].append(QLabel())
            self.map_img_label[21][y].resize(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            img = QPixmap("images/PacMan1.png").scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            self.map_img[21].append(img)
            self.map_img_label[21][y].setPixmap(self.map_img[21][y])
            self.map_img_layout.addWidget(self.map_img_label[21][y], 22, y, 1, 1)
        self.map_img_label[21].append(QLabel())
        self.map_img_label[21][3].setStyleSheet("color: white;"
                                                "background-color: #000000")
        self.map_img_layout.addWidget(self.map_img_label[21][3], 22, 3, 1, 16)
        # Trim White Spaces
        self.map_img_layout.setContentsMargins(0, 0, 0, 0)
        self.map_img_layout.setSpacing(0)
        self.setLayout(self.map_img_layout)
        winsound.PlaySound("musics/pacman_beginning.wav", winsound.SND_ASYNC)

    def resetMapImage(self):
        self.game_time = 0
        self.die = False
        self.scoreboard.setText(str(self.score))
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

    def displayMap(self):
        self.scoreboard.setText(str(self.score))
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
                    file = "images/Ghost" + str(ghost_idx) + self.ghost[ghost_idx].getDirect() + str(
                        self.ghost[ghost_idx].getShape()) + ".png"
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))
                self.map_img[x][y] = img
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])
        for y in range(3):
            if self.life > y + 1:
                file = "images/PacMan1.png"
            else:
                file = "images/PacMan5.png"
            img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            self.map_img[21][y] = img
            self.map_img_label[21][y].setPixmap(self.map_img[21][y])

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

        fontDB = QFontDatabase()
        fontDB.addApplicationFont("emulogic.ttf")
        app.setFont(QFont("emulogic"))

        sys.exit(app.exec_())
    except:
        print(traceback.format_exc())
