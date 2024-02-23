from sparkdesk_web.core import SparkWeb
import threading
import tkinter as tk

import pygame
import time
import webbrowser
from urllib import parse
import tkinter.messagebox as msgbox
import re


def function1():
    # 请根据自己配置三个参数
    sparkWeb = SparkWeb(
        cookie="di_c_mti=2b2e4535-5afc-6474-a9a3-d94458740237; d_d_app_ver=1.4.0; daas_st={%22sdk_ver%22:%221.3.9%22%2C%22status%22:%220%22}; appid=150b4dfebe; d_d_ci=6ca0a4ec-d5e8-62ef-b126-11fd9d40ecfe; ssoSessionId=d9847b86-6250-44c8-93f2-d30dd11c8a67; account_id=18137447940; gt_local_id=qoBPbQqnG6nLjriac0pkMFSbE6IgBlNT+Ezb/zu3CQTd2a1UuNMIwA==",
        fd="224053",
        GtToken=" RzAwAGMkT/Rqc78hj0TjZQi0T2ocE/vMeGQ0nb88259+m2QmUI0hDDAF07Vi5MNF4WGHjFYeOSArwkqzU7NxmDPkGGaTm50wqTmX6wH/rh/OYiI7NR67JuXoYuVAReCSBRSWtG/WjXOaJJsKqsmx1ircnqk1525XBLg5a0pJ1JgSw5jxjqWd82970VUId0dP/55oH/yLhLu2yGfnqbj3h2wUtkUaoYDG6/WEi2nB6ThGWznuZ76LwX4C5gsH4fmA3OnrgbFre42oZhq08TzKl/O/fcmWT+JEP5GZLVLDiMHRYqfVL2X0R/ZlcbpKB6b0Lje5y22g+vbnx2WZoaH1jarKSLHXEBXkunG89sp0EtSlJzbXig+sUvMTXPrcpSwETEMtblZWg9ksaMrVgWn7eJsuJYCXEahjx1pjFqbiOU/jmD+QRL88YwWHFz787dOOKf0w0MTMw79owleuMIJ02iCdT1urPPz+3kSAeIl3ZUQQLERUVDVCUghjgaGDqpA+LTRUgXoti4sQrmxDgwP+/U0PbJatQ/0Z67G9XWt4MioxOg0GnGsZWSR4gozq6GFs5LfG0ytPI5erEY9pyfKejB8ItaZIAD56/ZLd/P7a1j+X+2yRuRrvm+2yYbf8UfTPrQkBVJxqSZRanEgrhlEGaFWLY4YGHtw8BZb9UPx7Ll50NeDNsziE+T/WpXS88v7YPKovF6akpPxblGBvtWURTZlEgnjhJMhd2qx7j5YjQa30OmF3jjSjlmaDF5hPBNN3Ie2egQ8ba6pd/jtwoEMt9AnaG/PFcH2wJMVHzBYmgF5y4l6eSSt1PbVbh5YyoApTN8Pm3hO9BlWkNE/lRlzs0HSlawZgf4/J5Bm2njeQTKqmtUFcuTNL4wXDR6qtk2mkG7BxYdLdAfmqmSyBrvMJIkUFHWoiRifSmWl/TlysMVcTJjtOD9fPMAHlnaDBvUeZaWtKWC+WFZ3VA5/isDlaK1lh/UcBLsEznnmjhQpWK7qIWcnvZVAFjLn9lRmwn0WidP4KTk/vCy9N2zl9TVt1NgjBcfGQdl7VzTz19b5ask2TDofH3jkPemvdJ3OkYrhvI2XRgfsfnM2JRdxBgFYf8PdsDw1b2DQANQCRRprcobgiyy6ZgG8bliclvvn4Rvg7+d6BR/Xbvg4zRxEfhOVoEdKF/MGfdVQjN8g8hTY7djDC8bX9pnPZxlEFgYJ9ZfVrM1zGguq7swmYBrluoskf0Kz8kj+mbQDM6g0GhdvRpSxSOuc+dSD2mcl9nMCWEzBROqkVd5QDc2xJkPG/xgvyTvQyT8Qhn4uNBuBlUMUSChSHFNzLncvWmMTKyT2iJsjLdAoAPAnaQEMAcQmQHHSNTKFNx+BJnjjXSd2Cm90aSwlZOffW8fMdYSmSX9o+HrPkMOvDjRPXu1ezPWY/qn5vUjLJoP1NpVpAUqg0JZ7Hsru7wI5KzTphBocuzo/8gY0trIak6lO3G6X9pboln+8mJ97+odLAYBV+GQUAepBV2aR5mX4wHzTYE014FhPol9Q114ni9wQ/bsD+55zvxW8QsfYKLJHXuSR4qG8GJ24KTAOPZuMfZnPwbfEQnFJ6cRxfoYfMxBToZhiaFdebhwLpAizEvbWEBeEF5BKL4l4aS1MkMrF3YDJDWQCED5wbfO/Rn6G+O669+tLZgpv3t2Upm4NYggmKozUk+8RxgbEA/9UzMgocz7EosPGd+yUCSjSmwaX1r9GWkLCtYiio6SYBXDvUjTorrHbM5p+ZUlpXophdIOjkfA=="
    )
    i = 0
    print('您好，这里是AI助手')
    print('请输入您的问题')
    while i < 1:
        chat = sparkWeb.create_continuous_chat()
        inp = input('')
        chat.chat(str(inp))
    pass


def function2():
    import webbrowser

    url = "https://superdoctranslator.com/convert"  # 将此替换为您想打开的URL
    webbrowser.open(url)

    pass


def function3():
    from lunar_python import Lunar

    def get_birth_info(year, month, day):
        # 将公历日期转换为农历日期
        lunar = Lunar.fromYmd(year, month, day)
        lunar_year, lunar_month, lunar_day = lunar.getYear(), lunar.getMonth(), lunar.getDay()

        # 计算生辰八字
        bazi = (lunar_year - 4) % 60 * 2 + lunar_month * 2 + lunar_day
        gan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
        zhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
        gan_index = bazi // 10
        zhi_index = bazi % 10

        return f"{gan[gan_index]}{zhi[zhi_index]}"

    if __name__ == "__main__":
        year = int(input("请输入出生年份："))
        month = int(input("请输入出生月份："))
        day = int(input("请输入出生日期："))

        birth_info = get_birth_info(year, month, day)
        print(f"您的生辰八字是：{birth_info}")


def function4():
    url = "https://ys.mihoyo.com/cloud/#/"  # 将此替换为您想打开的URL
    webbrowser.open(url)


def function5():
    import webbrowser
    url = 'https://sr.mihoyo.com/cloud/?utm_source=official#/'
    webbrowser.open(url)


def function6():
    pygame.mixer.init()

    pygame.mixer.music.load('dzmy/敲.mp3')

    # 设置窗口大小，以及名称
    screen = pygame.display.set_mode((1000, 800))
    pygame.display.set_caption("电子木鱼")

    img_gd = pygame.image.load("dzmy/gongde.jpg")
    img_muyu = pygame.image.load("dzmy/muyu.jpg")
    bc = pygame.image.load("dzmy/bc.jpg")
    # 设置功德显示位置，以及设置木鱼图片的初始位置
    rect1 = img_gd.get_rect().move(400, 150)
    rect2 = img_muyu.get_rect().move(300, 200)
    # 设置功德上升的速度,以及控制功德移动
    rect_move = rect1
    speed = [0, -100]
    # 显示木鱼
    screen.blit(img_muyu, rect2)

    # 设置移动函数
    def move(rect_move):
        i = 1
        while (i > 0):
            rect_init = rect_move
            rect_move = rect_move.move(speed)
            screen.blit(bc, rect_init)
            screen.blit(img_gd, rect_move)
            pygame.display.flip()
            time.sleep(0.1)
            i = i - 1
        screen.blit(bc, rect_move)

    while True:
        for event in pygame.event.get():
            if pygame.mouse.get_focused():
                # 获取光标所在的位置
                ball_x, ball_y = pygame.mouse.get_pos()
                # 检测鼠标点击事件
                if pygame.Rect.collidepoint(rect2, (ball_x, ball_y)) and event.type == pygame.MOUSEBUTTONDOWN:
                    # 想在敲击时有声音，添加以下注解代码即可：
                    pygame.mixer.music.play()
                    move(rect_move)
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()


def function7():
    import time
    from enum import IntEnum
    import pygame

    time = time.strftime("%Y-%m-%d %H:%M:%S")
    version = str(time)

    # 基础参数设置
    square_size = 40  # 单格的宽度（不是格数！是为了方便绘制棋盘用的变量
    chess_size = square_size // 2 - 2  # 棋子大小
    web_broad = 15  # 棋盘格数+1（nxn）
    map_w = web_broad * square_size  # 棋盘长度
    map_h = web_broad * square_size  # 棋盘高度
    info_w = 60  # 按钮界面宽度
    button_w = 120  # 按钮长宽
    button_h = 45
    screen_w = map_w  # 总窗口长宽
    screen_h = map_h + info_w

    # 地图绘制模块

    class MAP_ENUM(IntEnum):  # 用数字表示当前格的情况
        be_empty = 0,  # 无人下
        player1 = 1,  # 玩家一，执白
        player2 = 2,  # 玩家二，执黑
        out_of_range = 3,  # 出界

    class Map:  # 地图类
        def __init__(self, width, height):  # 构造函数
            self.width = width
            self.height = height
            self.map = [[0 for x in range(self.width)] for y in range(self.height)]  # 存储棋盘的二维数组
            self.steps = []  # 记录步骤先后

        def get_init(self):  # 重置棋盘
            for y in range(self.height):
                for x in range(self.width):
                    self.map[y][x] = 0
            self.steps = []

        def intoNextTurn(self, turn):  # 进入下一回合，交换下棋人
            if turn == MAP_ENUM.player1:
                return MAP_ENUM.player2
            else:
                return MAP_ENUM.player1

        def getLocate(self, x, y):  # 输入下标，返回具体位置
            map_x = x * square_size
            map_y = y * square_size
            return (map_x, map_y, square_size, square_size)  # 返回位置信息

        def getIndex(self, map_x, map_y):  # 输入具体位置，返回下标
            x = map_x // square_size
            y = map_y // square_size
            return (x, y)

        def isInside(self, map_x, map_y):  # 是否在有效范围内
            if (map_x <= 0 or map_x >= map_w or
                    map_y <= 0 or map_y >= map_h):
                return False
            return True

        def isEmpty(self, x, y):  # 当前格子是否已经有棋子
            return (self.map[y][x] == 0)

        def click(self, x, y, type):  # 点击的下棋动作
            self.map[y][x] = type.value  # 下棋
            self.steps.append((x, y))  # 记录步骤信息

        def printChessPiece(self, screen):  # 绘制棋子
            player_one = (255, 245, 238)  # 象牙白
            player_two = (41, 36, 33)  # 烟灰
            player_color = [player_one, player_two]
            for i in range(len(self.steps)):
                x, y = self.steps[i]
                map_x, map_y, width, height = self.getLocate(x, y)
                pos, radius = (map_x + width // 2, map_y + height // 2), chess_size
                turn = self.map[y][x]
                pygame.draw.circle(screen, player_color[turn - 1], pos, radius)  # 画

        def drawBoard(self, screen):  # 画棋盘
            color = (0, 0, 0)  # 线色
            for y in range(self.height):
                # 画横着的棋盘线
                start_pos, end_pos = (square_size // 2, square_size // 2 + square_size * y), (
                    map_w - square_size // 2, square_size // 2 + square_size * y)
                pygame.draw.line(screen, color, start_pos, end_pos, 1)
            for x in range(self.width):
                # 画竖着的棋盘线
                start_pos, end_pos = (square_size // 2 + square_size * x, square_size // 2), (
                    square_size // 2 + square_size * x, map_h - square_size // 2)
                pygame.draw.line(screen, color, start_pos, end_pos, 1)

    # 高级AI模块

    class SITUATION(IntEnum):  # 棋型
        NONE = 0,  # 无
        SLEEP_TWO = 1,  # 眠二
        LIVE_TWO = 2,  # 活二
        SLEEP_THREE = 3,  # 眠三
        LIVE_THREE = 4,  # 活三
        CHONG_FOUR = 5,  # 冲四
        LIVE_FOUR = 6,  # 活四
        LIVE_FIVE = 7,  # 活五

    SITUATION_NUM = 8  # 长度

    # 方便后续调用枚举内容
    FIVE = SITUATION.LIVE_FIVE.value
    L4, L3, L2 = SITUATION.LIVE_FOUR.value, SITUATION.LIVE_THREE.value, SITUATION.LIVE_TWO.value
    S4, S3, S2 = SITUATION.CHONG_FOUR.value, SITUATION.SLEEP_THREE.value, SITUATION.SLEEP_TWO.value

    class MyChessAI():
        def __init__(self, chess_len):  # 构造函数
            self.len = chess_len  # 当前棋盘大小
            # 二维数组，每一格存的是：横评分，纵评分，左斜评分，右斜评分
            self.record = [[[0, 0, 0, 0] for i in range(chess_len)] for j in range(chess_len)]
            # 存储当前格具体棋型数量
            self.count = [[0 for i in range(SITUATION_NUM)] for j in range(2)]
            # 位置分（同条件下越靠近棋盘中央越高）
            self.position_isgreat = [
                [(web_broad - max(abs(i - web_broad / 2 + 1), abs(j - web_broad / 2 + 1))) for i in range(chess_len)]
                for j in range(chess_len)]

        def get_init(self):  # 初始化
            for i in range(self.len):
                for j in range(self.len):
                    for k in range(4):
                        self.record[i][j][k] = 0
            for i in range(len(self.count)):
                for j in range(len(self.count[0])):
                    self.count[i][j] = 0
            self.save_count = 0

        def isWin(self, board, turn):  # 当前人胜利
            return self.evaluate(board, turn, True)

        # 返回所有未下棋坐标（位置从好到坏）
        def genmove(self, board, turn):
            moves = []
            for y in range(self.len):
                for x in range(self.len):
                    if board[y][x] == 0:
                        score = self.position_isgreat[y][x]
                        moves.append((score, x, y))
            moves.sort(reverse=True)
            return moves

        # 返回当前最优解下标
        def search(self, board, turn):
            moves = self.genmove(board, turn)
            bestmove = None
            max_score = -99999  # 无穷小
            for score, x, y in moves:
                board[y][x] = turn.value
                score = self.evaluate(board, turn)
                board[y][x] = 0
                if score > max_score:
                    max_score = score
                    bestmove = (max_score, x, y)
            return bestmove

        # 主要用于测试的函数，现在已经没什么用
        def findBestChess(self, board, turn):
            # time1 = time.time()
            score, x, y = self.search(board, turn)
            # time2 = time.time()
            # print('time:%f  (%d, %d)' % ((time2 - time1), x, y))
            return (x, y)

        # 得出一点的评分
        # 直接列举所有棋型
        def getScore(self, mychess, yourchess):
            mscore, oscore = 0, 0
            if mychess[FIVE] > 0:
                return (10000, 0)
            if yourchess[FIVE] > 0:
                return (0, 10000)
            if mychess[S4] >= 2:
                mychess[L4] += 1
            if yourchess[L4] > 0:
                return (0, 9050)
            if yourchess[S4] > 0:
                return (0, 9040)
            if mychess[L4] > 0:
                return (9030, 0)
            if mychess[S4] > 0 and mychess[L3] > 0:
                return (9020, 0)
            if yourchess[L3] > 0 and mychess[S4] == 0:
                return (0, 9010)
            if (mychess[L3] > 1 and yourchess[L3] == 0 and yourchess[S3] == 0):
                return (9000, 0)
            if mychess[S4] > 0:
                mscore += 2000
            if mychess[L3] > 1:
                mscore += 500
            elif mychess[L3] > 0:
                mscore += 100
            if yourchess[L3] > 1:
                oscore += 2000
            elif yourchess[L3] > 0:
                oscore += 400
            if mychess[S3] > 0:
                mscore += mychess[S3] * 10
            if yourchess[S3] > 0:
                oscore += yourchess[S3] * 10
            if mychess[L2] > 0:
                mscore += mychess[L2] * 4
            if yourchess[L2] > 0:
                oscore += yourchess[L2] * 4
            if mychess[S2] > 0:
                mscore += mychess[S2] * 4
            if yourchess[S2] > 0:
                oscore += yourchess[S2] * 4
            return (mscore, oscore)  # 自我辅助效果，counter对面效果

        # 对上述得分进行进一步处理
        def evaluate(self, board, turn, checkWin=False):
            self.get_init()
            if turn == MAP_ENUM.player1:
                me = 1
                you = 2
            else:
                me = 2
                you = 1
            for y in range(self.len):
                for x in range(self.len):
                    if board[y][x] == me:
                        self.evaluatePoint(board, x, y, me, you)
                    elif board[y][x] == you:
                        self.evaluatePoint(board, x, y, you, me)
            mychess = self.count[me - 1]
            yourchess = self.count[you - 1]
            if checkWin:
                return mychess[FIVE] > 0  # 检查是否已经胜利
            else:
                mscore, oscore = self.getScore(mychess, yourchess)
                return (mscore - oscore)  # 自我辅助效果，counter对面效果

        def evaluatePoint(self, board, x, y, me, you):
            direction = [(1, 0), (0, 1), (1, 1), (1, -1)]  # 四个方向
            for i in range(4):
                if self.record[y][x][i] == 0:
                    # 检查当前方向棋型
                    self.getBasicSituation(board, x, y, i, direction[i], me, you, self.count[me - 1])
                else:
                    self.save_count += 1

        # 把当前方向棋型存储下来，方便后续使用
        def getLine(self, board, x, y, direction, me, you):
            line = [0 for i in range(9)]
            # “光标”移到最左端
            tmp_x = x + (-5 * direction[0])
            tmp_y = y + (-5 * direction[1])
            for i in range(9):
                tmp_x += direction[0]
                tmp_y += direction[1]
                if (tmp_x < 0 or tmp_x >= self.len or tmp_y < 0 or tmp_y >= self.len):
                    line[i] = you  # 出界
                else:
                    line[i] = board[tmp_y][tmp_x]
            return line

        # 把当前方向的棋型识别成具体情况（如把MMMMX识别成冲四）
        def getBasicSituation(self, board, x, y, dir_index, dir, me, you, count):
            # record赋值
            def setRecord(self, x, y, left, right, dir_index, direction):
                tmp_x = x + (-5 + left) * direction[0]
                tmp_y = y + (-5 + left) * direction[1]
                for i in range(left, right):
                    tmp_x += direction[0]
                    tmp_y += direction[1]
                    self.record[tmp_y][tmp_x][dir_index] = 1

            empty = MAP_ENUM.be_empty.value
            left_index, right_index = 4, 4
            line = self.getLine(board, x, y, dir, me, you)
            while right_index < 8:
                if line[right_index + 1] != me:
                    break
                right_index += 1
            while left_index > 0:
                if line[left_index - 1] != me:
                    break
                left_index -= 1
            left_range, right_range = left_index, right_index
            while right_range < 8:
                if line[right_range + 1] == you:
                    break
                right_range += 1
            while left_range > 0:
                if line[left_range - 1] == you:
                    break
                left_range -= 1
            chess_range = right_range - left_range + 1
            if chess_range < 5:
                setRecord(self, x, y, left_range, right_range, dir_index, dir)
                return SITUATION.NONE
            setRecord(self, x, y, left_index, right_index, dir_index, dir)
            m_range = right_index - left_index + 1
            if m_range == 5:
                count[FIVE] += 1
            # 活四冲四
            if m_range == 4:
                left_empty = right_empty = False
                if line[left_index - 1] == empty:
                    left_empty = True
                if line[right_index + 1] == empty:
                    right_empty = True
                if left_empty and right_empty:
                    count[L4] += 1
                elif left_empty or right_empty:
                    count[S4] += 1
            # 活三眠三
            if m_range == 3:
                left_empty = right_empty = False
                left_four = right_four = False
                if line[left_index - 1] == empty:
                    if line[left_index - 2] == me:  # MXMMM
                        setRecord(self, x, y, left_index - 2, left_index - 1, dir_index, dir)
                        count[S4] += 1
                        left_four = True
                    left_empty = True
                if line[right_index + 1] == empty:
                    if line[right_index + 2] == me:  # MMMXM
                        setRecord(self, x, y, right_index + 1, right_index + 2, dir_index, dir)
                        count[S4] += 1
                        right_four = True
                    right_empty = True
                if left_four or right_four:
                    pass
                elif left_empty and right_empty:
                    if chess_range > 5:  # XMMMXX, XXMMMX
                        count[L3] += 1
                    else:  # PXMMMXP
                        count[S3] += 1
                elif left_empty or right_empty:  # PMMMX, XMMMP
                    count[S3] += 1
            # 活二眠二
            if m_range == 2:
                left_empty = right_empty = False
                left_three = right_three = False
                if line[left_index - 1] == empty:
                    if line[left_index - 2] == me:
                        setRecord(self, x, y, left_index - 2, left_index - 1, dir_index, dir)
                        if line[left_index - 3] == empty:
                            if line[right_index + 1] == empty:  # XMXMMX
                                count[L3] += 1
                            else:  # XMXMMP
                                count[S3] += 1
                            left_three = True
                        elif line[left_index - 3] == you:  # PMXMMX
                            if line[right_index + 1] == empty:
                                count[S3] += 1
                                left_three = True
                    left_empty = True
                if line[right_index + 1] == empty:
                    if line[right_index + 2] == me:
                        if line[right_index + 3] == me:  # MMXMM
                            setRecord(self, x, y, right_index + 1, right_index + 2, dir_index, dir)
                            count[S4] += 1
                            right_three = True
                        elif line[right_index + 3] == empty:
                            # setRecord(self, x, y, right_index+1, right_index+2, dir_index, dir)
                            if left_empty:  # XMMXMX
                                count[L3] += 1
                            else:  # PMMXMX
                                count[S3] += 1
                            right_three = True
                        elif left_empty:  # XMMXMP
                            count[S3] += 1
                            right_three = True
                    right_empty = True
                if left_three or right_three:
                    pass
                elif left_empty and right_empty:  # XMMX
                    count[L2] += 1
                elif left_empty or right_empty:  # PMMX, XMMP
                    count[S2] += 1
            # 特殊活二眠二（有空格
            if m_range == 1:
                left_empty = right_empty = False
                if line[left_index - 1] == empty:
                    if line[left_index - 2] == me:
                        if line[left_index - 3] == empty:
                            if line[right_index + 1] == you:  # XMXMP
                                count[S2] += 1
                    left_empty = True
                if line[right_index + 1] == empty:
                    if line[right_index + 2] == me:
                        if line[right_index + 3] == empty:
                            if left_empty:  # XMXMX
                                count[L2] += 1
                            else:  # PMXMX
                                count[S2] += 1
                    elif line[right_index + 2] == empty:
                        if line[right_index + 3] == me and line[right_index + 4] == empty:  # XMXXMX
                            count[L2] += 1
            # 以上都不是则为none棋型
            return SITUATION.NONE

    # 主程序实现部分

    # 控制进程按钮类（父类）
    class Button:
        def __init__(self, screen, text, x, y, color, enable):  # 构造函数
            self.screen = screen
            self.width = button_w
            self.height = button_h
            self.button_color = color
            self.text_color = (255, 255, 255)  # 纯白
            self.enable = enable
            self.font = pygame.font.SysFont(None, button_h * 2 // 3)
            self.rect = pygame.Rect(0, 0, self.width, self.height)
            self.rect.topleft = (x, y)
            self.text = text
            self.init_msg()

        # 重写pygame内置函数，初始化我们的按钮
        def init_msg(self):
            if self.enable:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
            else:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center

        # 根据按钮enable状态填色，具体颜色在后续子类控制
        def draw(self):
            if self.enable:
                self.screen.fill(self.button_color[0], self.rect)
            else:
                self.screen.fill(self.button_color[1], self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)

    class WhiteStartButton(Button):  # 开始按钮（选白棋）
        def __init__(self, screen, text, x, y):  # 构造函数
            super().__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

        def click(self, game):  # 点击，pygame内置方法
            if self.enable:  # 启动游戏并初始化，变换按钮颜色
                game.start()
                game.winner = None
                game.multiple = False
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
                self.enable = False
                return True
            return False

        def unclick(self):  # 取消点击
            if not self.enable:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
                self.enable = True

    class BlackStartButton(Button):  # 开始按钮（选黑棋）
        def __init__(self, screen, text, x, y):  # 构造函数
            super().__init__(screen, text, x, y, [(26, 173, 25), (158, 217, 157)], True)

        def click(self, game):  # 点击，pygame内置方法
            if self.enable:  # 启动游戏并初始化，变换按钮颜色，安排AI先手
                game.start()
                game.winner = None
                game.multiple = False
                game.useAI = True
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
                self.enable = False
                return True
            return False

        def unclick(self):  # 取消点击
            if not self.enable:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
                self.enable = True

    class GiveupButton(Button):  # 投降按钮（任何模式都能用
        def __init__(self, screen, text, x, y):
            super().__init__(screen, text, x, y, [(230, 67, 64), (236, 139, 137)], False)

        def click(self, game):  # 结束游戏，判断赢家
            if self.enable:
                game.is_play = False
                if game.winner is None:
                    game.winner = game.map.intoNextTurn(game.player)
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
                self.enable = False
                return True
            return False

        def unclick(self):  # 保持不变，填充颜色
            if not self.enable:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
                self.enable = True

    class MultiStartButton(Button):  # 开始按钮（多人游戏）
        def __init__(self, screen, text, x, y):  # 构造函数
            super().__init__(screen, text, x, y, [(153, 51, 250), (221, 160, 221)], True)  # 紫色

        def click(self, game):  # 点击，pygame内置方法
            if self.enable:  # 启动游戏并初始化，变换按钮颜色
                game.start()
                game.winner = None
                game.multiple = True
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[1])
                self.enable = False
                return True
            return False

        def unclick(self):  # 取消点击
            if not self.enable:
                self.msg_image = self.font.render(self.text, True, self.text_color, self.button_color[0])
                self.enable = True

    class Game:  # pygame类,以下所有功能都是根据需要重写
        def __init__(self, caption):
            pygame.init()
            self.screen = pygame.display.set_mode([screen_w, screen_h])
            pygame.display.set_caption(caption)
            self.clock = pygame.time.Clock()
            self.buttons = []
            self.buttons.append(WhiteStartButton(self.screen, 'choose white', 20, map_h))
            self.buttons.append(BlackStartButton(self.screen, 'choose black', 190, map_h))
            self.buttons.append(GiveupButton(self.screen, 'surrdender', 360, map_h))
            self.buttons.append(MultiStartButton(self.screen, 'Multiple', 530, map_h))
            self.is_play = False
            self.map = Map(web_broad, web_broad)
            self.player = MAP_ENUM.player1
            self.action = None
            self.AI = MyChessAI(web_broad)
            self.useAI = False
            self.winner = None
            self.multiple = False

        def start(self):
            self.is_play = True
            self.player = MAP_ENUM.player1  # 白棋先手
            self.map.get_init()

        def play(self):
            # 画底板
            self.clock.tick(60)
            wood_color = (210, 180, 140)
            pygame.draw.rect(self.screen, wood_color, pygame.Rect(0, 0, map_w, screen_h))
            pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(map_w, 0, info_w, screen_h))
            # 画按钮
            for button in self.buttons:
                button.draw()
            if self.is_play and not self.isOver():
                if self.useAI and not self.multiple:
                    x, y = self.AI.findBestChess(self.map.map, self.player)
                    self.checkClick(x, y, True)
                    self.useAI = False
                if self.action is not None:
                    self.checkClick(self.action[0], self.action[1])
                    self.action = None
                if not self.isOver():
                    self.changeMouseShow()
            if self.isOver():
                self.showWinner()
                # self.buttons[0].enable = True
                # self.buttons[1].enable = True
                # self.buttons[2].enable = False
            self.map.drawBoard(self.screen)
            self.map.printChessPiece(self.screen)

        def changeMouseShow(self):  # 开始游戏的时候把鼠标预览切换成预览棋子的样子
            map_x, map_y = pygame.mouse.get_pos()
            x, y = self.map.getIndex(map_x, map_y)
            if self.map.isInside(map_x, map_y) and self.map.isEmpty(x, y):  # 在棋盘内且当前无棋子
                pygame.mouse.set_visible(False)
                smoke_blue = (176, 224, 230)
                pos, radius = (map_x, map_y), chess_size
                pygame.draw.circle(self.screen, smoke_blue, pos, radius)
            else:
                pygame.mouse.set_visible(True)

        def checkClick(self, x, y, isAI=False):  # 后续处理
            self.map.click(x, y, self.player)
            if self.AI.isWin(self.map.map, self.player):
                self.winner = self.player
                self.click_button(self.buttons[2])
            else:
                self.player = self.map.intoNextTurn(self.player)
                if not isAI:
                    self.useAI = True

        def mouseClick(self, map_x, map_y):  # 处理下棋动作
            if self.is_play and self.map.isInside(map_x, map_y) and not self.isOver():
                x, y = self.map.getIndex(map_x, map_y)
                if self.map.isEmpty(x, y):
                    self.action = (x, y)

        def isOver(self):  # 中断条件
            return self.winner is not None

        def showWinner(self):  # 输出胜者
            def showFont(screen, text, location_x, locaiton_y, height):
                font = pygame.font.SysFont(None, height)
                font_image = font.render(text, True, (255, 215, 0), (255, 255, 255))  # 金黄色
                font_image_rect = font_image.get_rect()
                font_image_rect.x = location_x
                font_image_rect.y = locaiton_y
                screen.blit(font_image, font_image_rect)

            if self.winner == MAP_ENUM.player1:
                str = 'White Wins!'
            else:
                str = 'Black Wins!'
            showFont(self.screen, str, map_w / 5, screen_h / 8, 100)  # 居上中，字号100
            pygame.mouse.set_visible(True)

        def click_button(self, button):
            if button.click(self):
                for tmp in self.buttons:
                    if tmp != button:
                        tmp.unclick()

        def check_buttons(self, mouse_x, mouse_y):
            for button in self.buttons:
                if button.rect.collidepoint(mouse_x, mouse_y):
                    self.click_button(button)
                    break

    # 以下为pygame1.9帮助文档的示例代码
    if __name__ == '__main__':
        game = Game(version)
        while True:
            game.play()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    game.mouseClick(mouse_x, mouse_y)
                    game.check_buttons(mouse_x, mouse_y)


def function8():
    import webbrowser

    url = input("请输入链接：")
    final_url = "https://vip.bljiex.com/?v=" + url
    webbrowser.open(final_url)


def function9():
    import webbrowser

    url = ('https://www.jbsou.cn/?')
    url_search = input('输入音乐名称')
    final_url = url + 'name=' + url_search + "&type=netease"
    webbrowser.open(final_url)


def function10():
    import requests
    xz = input('请输入您的星座')
    xz = xz.strip('座')
    url = "https://eolink.o.apispace.com/xzcx/api/v1/xzw/constellation_query/"

    payload = {"keyword": xz}

    headers = {
        "X-APISpace-Token": "6971646da11549e6aeec510fae96123d"
    }

    response = requests.request("GET", url, params=payload, headers=headers)

    print(response.text)


def function11():
    import requests
    jg = input('请输入您梦到的事情')
    url = "https://eolink.o.apispace.com/zgjm/common/dream/searchDreamDetail"

    payload = {"keyword": jg}

    headers = {
        "X-APISpace-Token": "6971646da11549e6aeec510fae96123d",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.request("POST", url, data=payload, headers=headers)


    print(response.text)


def start_thread(func):
    threading.Thread(target=func).start()


root = tk.Tk()
root.title('windows助手')
root.geometry('256x330')

button1 = tk.Button(root, text="           AI助手           ", command=lambda: start_thread(function1))
button2 = tk.Button(root, text="        PDF转Word      ", command=lambda: start_thread(function2))
button3 = tk.Button(root, text='          电子木鱼         ', command=lambda: start_thread(function6))
button4 = tk.Button(root, text="          原神启动         ", command=lambda: start_thread(function4))
button5 = tk.Button(root, text="          崩铁启动         ", command=lambda: start_thread(function5))
button6 = tk.Button(root, text="          生辰八字         ", command=lambda: start_thread(function3))
button7 = tk.Button(root, text='          ai五子棋          ', command=lambda: start_thread(function7))
button8 = tk.Button(root, text='          视频解析          ', command=lambda: start_thread(function8))
button9 = tk.Button(root, text='          音乐下载          ', command=lambda: start_thread(function9))
button10 =  tk.Button(root, text='          星座运势          ', command=lambda: start_thread(function10))
button11 = tk.Button(root, text='          周公解梦          ', command=lambda: start_thread(function11))


button1.pack()
button2.pack()
button3.pack()
button4.pack()
button5.pack()
button6.pack()
button7.pack()
button8.pack()
button9.pack()
button10.pack()
button11.pack()
root.mainloop()
