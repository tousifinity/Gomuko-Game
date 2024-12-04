from time import sleep
import pygame
from pygame.locals import *
from random import randint

level = 15
grade = 10
MAX = 1008611


def Scan(chesspad, color):
    shape = [[[0 for high in range(5)] for col in range(15)]
             for row in range(15)]
    # Scan each point, and then make a value evaluation in each direction of the blank point! !
    for i in range(15):
        for j in range(15):

            # If this is empty, then the surrounding area can be scanned
            if chesspad[i][j] == 0:
                m = i
                n = j
                # If the above is consistent with the currently passed color parameter, then add points to 0!
                while n - 1 >= 0 and chesspad[m][n - 1] == color:
                    n -= 1
                    shape[i][j][0] += grade
                if n-1 >= 0 and chesspad[m][n - 1] == 0:
                    shape[i][j][0] += 1
                if n-1 >= 0 and chesspad[m][n - 1] == -color:
                    shape[i][j][0] -= 2
                m = i
                n = j
                # If the bottom is consistent with the currently passed color parameter, then add points to 0!
                while (n + 1 < level and chesspad[m][n + 1] == color):
                    n += 1
                    shape[i][j][0] += grade
                if n + 1 < level and chesspad[m][n + 1] == 0:
                    shape[i][j][0] += 1
                if n + 1 < level and chesspad[m][n + 1] == -color:
                    shape[i][j][0] -= 2
                m = i
                n = j
                # If the left side is consistent with the currently passed color parameter, then add 1 point!
                while (m - 1 >= 0 and chesspad[m - 1][n] == color):
                    m -= 1
                    shape[i][j][1] += grade
                if m - 1 >= 0 and chesspad[m - 1][n] == 0:
                    shape[i][j][1] += 1
                if m - 1 >= 0 and chesspad[m - 1][n] == -color:
                    shape[i][j][1] -= 2
                m = i
                n = j
                # If the right side is consistent with the currently passed color parameter, then add 1 point!
                while (m + 1 < level and chesspad[m + 1][n] == color):
                    m += 1
                    shape[i][j][1] += grade
                if m + 1 < level and chesspad[m + 1][n] == 0:
                    shape[i][j][1] += 1
                if m + 1 < level and chesspad[m + 1][n] == -color:
                    shape[i][j][1] -= 2
                m = i
                n = j
                # If the lower left is consistent with the currently passed color parameter, then add 2 points!
                while (m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == color):
                    m -= 1
                    n += 1
                    shape[i][j][2] += grade
                if m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == 0:
                    shape[i][j][2] += 1
                if m - 1 >= 0 and n + 1 < level and chesspad[m - 1][n + 1] == -color:
                    shape[i][j][2] -= 2
                m = i
                n = j
                # If the upper right is consistent with the currently passed color parameter, then add 2 points!
                while (m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == color):
                    m += 1
                    n -= 1
                    shape[i][j][2] += grade
                if m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == 0:
                    shape[i][j][2] += 1
                if m + 1 < level and n - 1 >= 0 and chesspad[m + 1][n - 1] == -color:
                    shape[i][j][2] -= 2
                m = i
                n = j
                # If the upper left is consistent with the currently passed color parameter, then add 3 points!
                while (m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == color):
                    m -= 1
                    n -= 1
                    shape[i][j][3] += grade
                if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == 0:
                    shape[i][j][3] += 1
                if m - 1 >= 0 and n - 1 >= 0 and chesspad[m - 1][n - 1] == -color:
                    shape[i][j][3] -= 2
                m = i
                n = j
                # If the bottom right is consistent with the currently passed color parameter, then add 3 points!
                while m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == color:
                    m += 1
                    n += 1
                    shape[i][j][3] += grade
                if m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == 0:
                    shape[i][j][3] += 1
                if m + 1 < level and n + 1 < level and chesspad[m + 1][n + 1] == -color:
                    shape[i][j][3] -= 2
    return shape


def Sort(shape):
    for i in shape:
        for j in i:
            for x in range(5):
                for w in range(3, x - 1, -1):
                    if j[w - 1] < j[w]:
                        temp = j[w]
                        j[w - 1] = j[w]
                        j[w] = temp
    print("This Time Sort Done !")
    return shape


def Evaluate(shape):
    for i in range(level):
        for j in range(level):

            if shape[i][j][0] == 4:
                return i, j, MAX
            shape[i][j][4] = shape[i][j][0]*1000 + shape[i][j][1] * \
                100 + shape[i][j][2]*10 + shape[i][j][3]
    max_x = 0
    max_y = 0
    max = 0
    for i in range(15):
        for j in range(15):
            if max < shape[i][j][4]:
                max = shape[i][j][4]
                max_x = i
                max_y = j
    print("the max is " + str(max) + " at ( " + str(max_x)+" , "+str(max_y)+" )")
    return max_x, max_y, max


class chess(object):
    def __init__(self):
        self.a = [[0 for high in range(15)] for col in range(15)]

    def fall(self, x, y, color):
        if (x < 0 or x > level - 1 or y < 0 or y > level - 1):
            return
        self.a[x][y] = color
        if Judge(x, y, color, self.a, 4):
            if color < 0:
                print("The Winner is White!!")
            else:
                print("The Winner is Black!!")

    def isEmpty(self, m, n):
        if self.a[m][n] != 0:
            return False
        else:
            return True


def Judge(x, y, color, CHESSLOCATION, length):
    count1, count2, count3, count4 = 0, 0, 0, 0
    # Horizontal judgment
    i = x - 1
    while (i >= 0):
        if color == CHESSLOCATION[i][y]:
            count1 += 1
            i -= 1
        else:
            break
    i = x + 1
    while i < level:
        if CHESSLOCATION[i][y] == color:
            count1 += 1
            i += 1
        else:
            break

    # vertical judgment
    j = y - 1
    while (j >= 0):
        if CHESSLOCATION[x][j] == color:
            count2 += 1
            j -= 1
        else:
            break
    j = y + 1
    while j < level:
        if CHESSLOCATION[x][j] == color:
            count2 += 1
            j += 1
        else:
            break

    # Positive diagonal judgment
    i, j = x - 1, y - 1
    while (i >= 0 and j >= 0):
        if CHESSLOCATION[i][j] == color:
            count3 += 1
            i -= 1
            j -= 1
        else:
            break
    i, j = x + 1, y + 1
    while (i < level and j < level):
        if CHESSLOCATION[i][j] == color:
            count3 += 1
            i += 1
            j += 1
        else:
            break
    # Anti-diagonal judgment
    i, j = x + 1, y - 1
    while (i < level and j >= 0):
        if CHESSLOCATION[i][j] == color:
            count4 += 1
            i += 1
            j -= 1
        else:
            break
    i, j = x - 1, y + 1
    while (i > 0 and j < level):
        if CHESSLOCATION[i][j] == color:
            count4 += 1
            i -= 1
            j += 1
        else:
            break

    if count1 >= length or count2 >= length or count3 >= length or count4 >= length:
        return True
    else:
        return False


def Autoplay(ch, m, n):
    a1 = [1, -1, 1, -1, 1, -1, 0, 0]
    b1 = [1, -1, -1, 1, 0, 0, 1, -1]
    rand = randint(0, 7)
    while m+a1[rand] >= 0 and m+a1[rand] < level and n+b1[rand] >= 0 and n+b1[rand] < level and ch[m+a1[rand]][n+b1[rand]] != 0:
        rand = randint(0, 7)
    return m + a1[rand], n+b1[rand]


def BetaGo(ch, m, n, color, times):
    if times < 2:
        return Autoplay(ch, m, n)
    else:
        shape_P = Scan(ch, -color)
        shape_C = Scan(ch, color)
        shape_P = Sort(shape_P)
        shape_C = Sort(shape_C)
        max_x_P, max_y_P, max_P = Evaluate(shape_P)
        max_x_C, max_y_C, max_C = Evaluate(shape_C)
        if max_P > max_C and max_C < MAX:
            return max_x_P, max_y_P
        else:
            return max_x_C, max_y_C


def satrtGUI(ch):
    pygame.init()
    pygame.display.set_caption("Project 1.0 || GOMOKU || GROUP 2")

    bg = './GUI_Pic/BG1.png'
    white_image = './GUI_Pic/white.png'
    black_image = './GUI_Pic/black.png'

    screen = pygame.display.set_mode((750, 750), 0, 32)
    background = pygame.image.load(bg).convert()
    white = pygame.image.load(white_image).convert_alpha()
    black = pygame.image.load(black_image).convert_alpha()
    white = pygame.transform.smoothscale(
        white, (int(white.get_width() * 1.5), int(white.get_height() * 1.5)))
    black = pygame.transform.smoothscale(
        black, (int(black.get_width() * 1.5), int(black.get_height() * 1.5)))

    screen.blit(background, (0, 0))
    font = pygame.font.SysFont("Arial Bold", 40)

    pygame.event.set_blocked([1, 4, pygame.KEYUP, pygame.JOYAXISMOTION, pygame.JOYBALLMOTION,
                              pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION])
    pygame.event.set_allowed(
        [pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP, pygame.KEYDOWN])

    dot_list = [(25 + i * 50 - white.get_width() / 2, 25 + j * 50 -
                 white.get_height() / 2) for i in range(level) for j in range(level)]
    color = -1
    times = 0
    flag = False

    while not flag:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if 25 <= x <= 725 and 25 <= y <= 725 and ((x - 25) % 50 <= level or (x - 25) % 50 >= 0) and (
                        (y - 25) % 50 <= level or (y - 25) % 50 >= 0):
                    color = -1 * color
                    m = int(round((x - 25) / 50))
                    n = int(round((y - 25) / 50))
                    if not ch.isEmpty(m, n):
                        print("Black OverWrite~~")
                        continue
                    ch.fall(m, n, color)
                    screen.blit(black, dot_list[level * m + n])
                    if Judge(m, n, color, ch.a, 4):
                        game_over_text = font.render(
                            'GAME OVER, Black is win!', True, (110, 210, 30))
                        background_rect = pygame.Rect(
                            80, 650, game_over_text.get_width(), game_over_text.get_height())
                        pygame.draw.rect(
                            screen, (255, 255, 255), background_rect)
                        screen.blit(game_over_text, (80, 650))
                        flag = True
                        break

                    color = -1 * color
                    sleep(0.1)
                    x, y = BetaGo(ch.a, m, n, color, times)
                    times += 1
                    print("Predict:" + str(x) + " and " + str(y))
                    ch.fall(x, y, color)
                    screen.blit(white, dot_list[level * x + y])
                    if Judge(x, y, color, ch.a, 4):
                        game_over_text = font.render(
                            'GAME OVER, White is win!', True, (217, 20, 30))
                        background_rect = pygame.Rect(
                            80, 650, game_over_text.get_width(), game_over_text.get_height())
                        pygame.draw.rect(
                            screen, (255, 255, 255), background_rect)
                        screen.blit(game_over_text, (80, 650))
                        flag = True
                        break
        pygame.display.update()
        if flag:
            sleep(10)


now = chess()
satrtGUI(now)


# Made by Tousif
