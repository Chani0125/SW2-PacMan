from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from player import PacMan
from enemy import Ghost

import traceback
import winsound

# 방향에 대한 튜플 정보는 모두 (동, 서, 남, 북)으로 저장되어있음 - 0: 못 감, 1: 갈 수 있음
# 방향에 대한 정수 정보 - 0: 동, 1: 서, 2: 남, 3: 북

class PacManGame(QWidget):
    # 초기 맵 상태 저장
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

    # 게임 진행 맵 상태 저장
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

    # 교차로 정보 저장
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

    # 교차로 방향 정보 저장
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

    # 맵 이미지 파일 번호 및 회전 횟수 저장
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

    # 상수

    # 게임 크기 간격
    DISPLAY_SIZE = 2

    # 게임 속도 간격 (ms)
    INTERVAL = 50

    # 팩맨 움직임 간격
    PACMAN_INTERVAL = 6

    # 유령 움직임 간격
    GHOST_INTERVAL = 5

    # 유령 나오는 시간 간격
    GHOST_SPAWN_INTERVAL = 125

    # 죽었을 때 모션 간격
    DEATH_INTERVAL = 3

    def __init__(self):
        super().__init__()

        # 창 세팅
        self.setWindowTitle('PacMan Game')

        # 기본 변수 세팅
        self.score = 0
        self.life = 3
        self.num_cookie = 150
        self.game_time = 0
        self.game_total_time = 0
        self.die = False
        self.over = False
        self.game_over = False

        # 초기 화면 설정
        self.setInitMapImage()

        # 팩맨 및 유령 객체 생성
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]

        # INTERVAL마다 해당 함수 실행
        self.timer = QTimer(self)
        self.timer.start(self.INTERVAL)
        self.timer.timeout.connect(self.intervalEvent)

    # 게임을 초기 세팅으로 돌린다
    # 팩맨이 유령에게 잡혔을 때 사용
    def resetGame(self):
        # 맵 초기화
        self.resetMapImage()
        # 객체 초기화
        self.pacman = PacMan()
        self.ghost = [
            Ghost(1, 0, 7, 9, True),
            Ghost(2, 0, 9, 9, False),
            Ghost(3, 0, 9, 8, False),
            Ghost(3, 0, 9, 10, False)
        ]

    # 화면에 OVER!을 출력하고 게임을 종료시킨다
    def gameOver(self):
        # 게임의 중앙 부분의 Lable에 텍스트를 출력시킨다
        for y in range(7, 12):
            # 텍스트 설정
            self.map_img_label[11][y].setText("OVER!"[y - 7])
            # 스타일 설정
            over_font = self.map_img_label[11][y].font()
            over_font.setPointSize(18)
            if self.over:  # 목숨이 다 없어져 게임 오버 된 경우
                self.map_img_label[11][y].setStyleSheet("color: yellow;"
                                                        "background-color: #000000")
            else:  # 쿠키를 다 먹어 게임 오버 된 경우
                self.map_img_label[11][y].setStyleSheet("color: green;"
                                                        "background-color: #000000")
            self.map_img_label[11][y].setFont(over_font)
            self.map_img_label[11][y].setAlignment(Qt.AlignCenter)
        # 더 이상 게임이 움직이 않도록 해준다
        self.game_over = True

    # 매 INTERVAL마다 실행되는 함수
    # 게임의 핵심적인 역할을 수행한다
    def intervalEvent(self):
        try:
            # 게임이 종료되었는지 확인
            if self.game_over:
                return
            # 게임이 시작될 때 까지 기다린다
            self.game_total_time += 1
            if self.game_total_time > 3000 // self.INTERVAL:  # 게임 실행 후 3s 후 시작
                self.game_time += 1

                # 팩맨이 죽은 경우
                if self.die:
                    # 죽은 이후 일정 시간을 기다린 후 일정 시간마다 팩맨의 모션을 변화시킨다
                    if self.game_time % self.DEATH_INTERVAL == 0 and self.game_time >= self.DEATH_INTERVAL * 2:
                        if self.pacman.getShape() < 5:  # 팩맨의 모양을 바꾼다
                            self.pacman.changeShape(self.pacman.getShape() + 1)
                        else:
                            if self.over:  # 게임이 종료되었다면 게임 종료 함수를 호출
                                self.gameOver()
                                return
                            else:  # 목숨이 남아있다면 객체 배치 초기화
                                self.resetGame()
                else:
                    # 객체들이 움직이는 것처럼 모양을 바꾼다
                    self.pacman.changeShape()
                    for ghost in self.ghost:
                        if self.game_time % 2 == 0:
                            ghost.changeShape()

                # 화면 새로고침
                self.displayMap()
                self.displayEntities()

                # 쿠키를 다 먹은 경우 종료 조건 표시
                if self.num_cookie == 0:
                    self.gameOver()
                    return

                # 팩맨이 죽은 경우 현재 함수 종료
                if self.die:
                    return

                # 팩맨이 유령에게 잡힌 경우
                for ghost in self.ghost:  # 각 유령 객체마다 비교
                    if self.pacman.getLocation() == ghost.getLocation():  # 유령과 팩맨의 좌표가 일치하는 경우
                        self.die = True  # 죽었을 때 게임 진행을 위해 True로 변경
                        self.game_time = 0  # 게임 시간 초기화
                        self.life -= 1  # 목숨 감소
                        winsound.PlaySound("musics/pacman_death.wav", winsound.SND_ASYNC)
                        # 목숨을 모두 소진 한 경우
                        if self.life == 0:
                            self.over = True
                        return

                # 팩맨의 이동
                fore_pacman_x, fore_pacman_y = self.pacman.getForeLocation()  # 팩맨 앞 칸의 좌표
                # 맵 좌우의 포탈에 대한 경우 (동쪽)
                if fore_pacman_x == 9 and fore_pacman_y == 19:
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.setLocation(9, 0)
                # 맵 좌우의 포탈에 대한 경우 (서쪽)
                elif fore_pacman_x == 9 and fore_pacman_y == -1:
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.setLocation(9, 18)
                # 팩맨 앞에 벽이 있는 경우
                elif self.map_obj_info[fore_pacman_x][fore_pacman_y] == 0:
                    self.pacman.setShapeChange(False)
                # 팩맨 앞에 벽이 없는 경우
                else:
                    self.pacman.setShapeChange(True)
                    # 일정한 시간마다 팩맨을 움직인다
                    if self.game_time % self.PACMAN_INTERVAL == 0:
                        self.pacman.move()

                # 유령의 이동
                for ghost in self.ghost:  # 각 유령 객체마다 실행
                    # 활성화 된 유령이고 유령이 움직일 시간이면 유령이 움직임
                    if ghost.isActive() and self.game_time % self.GHOST_INTERVAL == 0:
                        ghost_x, ghost_y = ghost.getLocation()  # 유령의 좌표 정보
                        fore_ghost_x, fore_ghost_y = ghost.getForeLocation()  # 유령의 앞 칸의 좌표 정보
                        # 맵 좌우의 포탈에 대한 경우 (동쪽)
                        if fore_ghost_x == 9 and fore_ghost_y == 19:
                            ghost.setLocation(9, 0)
                        # 맵 좌우의 포탈에 대한 경우 (서쪽)
                        elif fore_pacman_x == 9 and fore_ghost_y == -1:
                            ghost.setLocation(9, 18)
                        # 유령이 현재 교차로에 서 있거나 앞에 벽이 있는 경우
                        elif self.map_int_info[ghost_x][ghost_y] == 1 or self.map_obj_info[fore_ghost_x][
                            fore_ghost_y] == 0:
                            # 현재 갈 수 있는 방향에 대한 튜플 정보
                            d = self.map_int_direct_info[ghost_x][ghost_y]
                            if self.map_int_info[ghost_x][ghost_y] == 0:  # 현재 교차로가 아닌 경우 (e.g. 꺽인 길)
                                for i in range(len(d)):
                                    # 갈 수 있는 길 중, 온 길이 아닌 곳을 택한다
                                    if d[i] == 1 and ghost.getOppositeDirect() != i:
                                        ghost.setDirect(i)
                                        break
                            else:  # 현재 교차로인 경우
                                direct_bnum = 0  # 방향에 대한 이진 수
                                for i in range(len(d)):
                                    if d[i] == 1 and ghost.getOppositeDirect() != i:
                                        direct_bnum += 2 ** i
                                # 유령의 방향을 랜덤하게 정하도록 갈 수 있는 방향에 대한 이진수를 넘긴다
                                ghost.changeDirect(direct_bnum)
                        # 유령을 움직인다
                        ghost.move()

                # 쿠키를 먹는 경우
                pacman_x, pacman_y = self.pacman.getLocation()  # 팩맨의 현재 위치
                if self.map_obj_info[pacman_x][pacman_y] == 2:  # 일반 쿠키를 먹는 경우
                    winsound.PlaySound("musics/pacman_chomp.wav", winsound.SND_ASYNC)
                    self.score += 10
                    self.num_cookie -= 1
                    self.map_obj_info[pacman_x][pacman_y] = 1
                elif self.map_obj_info[pacman_x][pacman_y] == 3:  # 파워 쿠키를 먹는 경우
                    winsound.PlaySound("musics/pacman_chomp.wav", winsound.SND_ASYNC)
                    self.score += 50
                    self.num_cookie -= 1
                    self.map_obj_info[pacman_x][pacman_y] = 1

                # 게임 시간 경과에 따라 유령을 소환한다
                # 두 번 째 유령 소환
                if self.game_time == self.GHOST_SPAWN_INTERVAL - self.GHOST_INTERVAL:
                    self.ghost[1].setLocation(8, 9)
                    self.ghost[1].setDirect(3)
                if self.game_time == self.GHOST_SPAWN_INTERVAL:
                    self.ghost[1].setLocation(7, 9)
                if self.game_time == self.GHOST_SPAWN_INTERVAL + self.GHOST_INTERVAL:
                    self.ghost[1].setActive(True)
                    self.ghost[1].changeDirect(3)
                    self.ghost[1].move()
                # 세 번 째 유령 소환
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
                # 네 번 째 유령 소환
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

    # 초기 맵 세팅
    def setInitMapImage(self):
        # GridLayout을 통해 GUI 표현
        self.map_img_layout = QGridLayout()

        # 점수판
        self.scoreboard = QLabel(str(self.score))
        self.scoreboard.setStyleSheet("color: white;"
                                      "background-color: #000000")
        self.scoreboard.setMargin(12)
        scoreboard_font = self.scoreboard.font()
        scoreboard_font.setPointSize(12)
        self.scoreboard.setFont(scoreboard_font)
        self.scoreboard.resize(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE * 19)
        self.map_img_layout.addWidget(self.scoreboard, 0, 0, 1, 19)

        # 메인 맵
        self.map_img_label = [list() for _ in range(len(self.map_img_info) + 1)]
        self.map_img = [list() for _ in range(len(self.map_img_info) + 1)]
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                if x == 11 and (6 < y < 12):
                    # READY 글자
                    self.map_img_label[x].append(QLabel("READY"[y - 7]))
                    ready_font = self.map_img_label[x][y].font()
                    ready_font.setPointSize(18)
                    self.map_img_label[x][y].setStyleSheet("color: yellow;"
                                                           "background-color: #000000")
                    self.map_img_label[x][y].setFont(ready_font)
                    self.map_img_label[x][y].setAlignment(Qt.AlignCenter)
                    # 좌표를 맞추기 위해 None을 삽입함
                    self.map_img[x].append(None)
                else:
                    # 맵 구조
                    self.map_img_label[x].append(QLabel())
                    self.map_img_label[x][y].resize(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
                    # 필요한 이미지 로드
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
                    img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)  # 크기 조정
                    img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))  # 회전
                    self.map_img[x].append(img)
                    self.map_img_label[x][y].setPixmap(self.map_img[x][y])
                # 레이아웃에 위젯 추가
                self.map_img_layout.addWidget(self.map_img_label[x][y], x + 1, y, 1, 1)

        # 목숨 출력
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

        # 레이아웃 공백 제거
        self.map_img_layout.setContentsMargins(0, 0, 0, 0)
        self.map_img_layout.setSpacing(0)
        self.setLayout(self.map_img_layout)

        # 게임 시작 사운드 재생
        winsound.PlaySound("musics/pacman_beginning.wav", winsound.SND_ASYNC)

    # 맵을 초기 세팅으로 되돌린다
    # 팩맨이 유령에게 잡힌 경우 사용
    def resetMapImage(self):
        self.game_time = 0  # 게임 시간 초기화
        self.die = False  # 죽음 여부 초기화
        self.scoreboard.setText(str(self.score))  # 점수 갱신

        # 객체 움직임 초기화
        for ghost in self.ghost:
            ghost.setActive(True)
        self.pacman.setShapeChange(True)

        # 필요한 이미지 로드 및 회전 후 출력
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
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)  #사이즈
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))  # 회전
                self.map_img[x].append(img)
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])

    # 배경 맵 출력
    def displayMap(self):
        # 점수판 갱신
        self.scoreboard.setText(str(self.score))

        # 메인 맵 출력
        for x in range(len(self.map_img_info)):
            for y in range(len(self.map_obj_info[x])):
                # 필요한 이미지 로드 및 회전 후 출력
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
                img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)  # 사이즈
                img = img.transformed(QTransform().rotate(self.map_img_info[x][y][1] * 90))  # 회전
                self.map_img[x][y] = img
                self.map_img_label[x][y].setPixmap(self.map_img[x][y])

        # 목숨 갯수 갱신
        for y in range(3):
            if self.life > y + 1:
                file = "images/PacMan1.png"
            else:
                file = "images/PacMan5.png"
            img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            self.map_img[21][y] = img
            self.map_img_label[21][y].setPixmap(self.map_img[21][y])

    # 팩맨 및 유령 출력
    # displayMap 함수 뒤에 사용
    def displayEntities(self):
        # 유령 출력
        for i in range(len(self.ghost)):
            x, y = self.ghost[i].getLocation()
            file = "images/Ghost" + str(i) + self.ghost[i].getDirect() + str(self.ghost[i].getShape()) + ".png"
            img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
            self.map_img[x][y] = img
            self.map_img_label[x][y].setPixmap(self.map_img[x][y])

        # 팩맨 출력
        x, y = self.pacman.getLocation()
        file = "images/PacMan" + str(self.pacman.getShape()) + ".png"
        img = QPixmap(file).scaled(15 * self.DISPLAY_SIZE, 15 * self.DISPLAY_SIZE)
        img = img.transformed(QTransform().rotate(self.pacman.getDirect() * 90))
        self.map_img[x][y] = img
        self.map_img_label[x][y].setPixmap(self.map_img[x][y])

    # 방향키에 따라 팩맨 방향 조정
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

        # 게임에 사용될 폰트 불러오기
        fontDB = QFontDatabase()
        fontDB.addApplicationFont("emulogic.ttf")
        app.setFont(QFont("emulogic"))

        sys.exit(app.exec_())
    except:
        print(traceback.format_exc())
