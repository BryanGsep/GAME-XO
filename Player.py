import random
import pygame
import tools
import os

curdir = os.path.dirname(__file__)


class Comp():
    # Define the constructor
    def __init__(self, N):  # Parameter is the size of the board (NxN)
        self.size = N
        self.board = []
        for i in range(N):
            self.board.append([])
            for j in range(N):
                self.board[i].append(' ')


    # Insert a letter in certain position in the board
    def insertLetter(self, other, letter, Vpos, Hpos):
        self.board[Vpos - 1][Hpos - 1] = letter
        other.board[Vpos -1][Hpos - 1] = letter


    # Determine whether or not the space is free
    def spaceIsFree(self, Vpos, Hpos):
        return self.board[Vpos - 1][Hpos - 1] == ' '


    def playerpoint(self, le, Vpos, Hpos):
        steps = [[1, 0], [0, 1], [1, 1], [1, -1]]  # Steps list
        points = []  # Point list for all directions
        for step in steps:
            # Find the largest effect range for current point
            effect_range = [0, 1]
            for i in range(1, 5):  # Move backward 4 steps
                Vcur = Vpos - i * step[0]
                Hcur = Hpos - i * step[1]
                if Vcur >= 1 and Vcur <= self.size and Hcur >= 1 and Hcur <= self.size:
                    if self.board[Vcur-1][Hcur-1] == le or self.board[Vcur-1][Hcur-1] == " ":
                        effect_range[0] -= 1
                    else:
                        break
                else:
                    break
            for i in range(1,5):  # Move forward 4 steps
                Vcur = Vpos + i * step[0]
                Hcur = Hpos + i * step[1]
                if Vcur >= 1 and Vcur <= self.size and Hcur >= 1 and Hcur <= self.size:
                    if self.board[Vcur-1][Hcur-1] == le or self.board[Vcur-1][Hcur-1] == " ":
                        effect_range[1] += 1
                    else:
                        break
                else:
                    break

            # Check range is larger than 5 or not
            if effect_range[1] - effect_range[0] < 5:
                points.append(0)  # If there is no available row
            else:  # if the range is larger than 5 then we check all possible options
                maxpoint = 0
                for i in range(effect_range[0], effect_range[1]-4):
                    point = 0
                    for j in range(i, i+5):
                        if self.board[Vpos + j * step[0]-1][Hpos + j * step[1]-1] == le:
                        # Plus one point if there is one letter in the range
                            point += 1
                    #Increase the chance that they would choose denser area
                    Vcur = Vpos+step[0]
                    Hcur = Hpos+step[1]
                    if Vcur >= 1 and Vcur <= self.size and Hcur >= 1 and Hcur <= self.size:
                        if self.board[Vcur -1][Hcur -1] == ' ':
                            point -= 0.25

                    Vcur = Vpos - step[0]
                    Hcur = Hpos - step[1]
                    if Vcur >= 1 and Vcur <= self.size and Hcur >= 1 and Hcur <= self.size:
                        if self.board[Vcur - 1][Hcur - 1] == ' ':
                            point -= 0.25
                    if i < 0 and i > -4:
                        point += 0.3

                    Vcur = Vpos + (i-1)*step[0]
                    Hcur = Hpos + (i-1)*step[1]
                    if Vcur < 1 or Vcur > self.size or Hcur < 1 or Hcur > self.size:
                        point -= 0.25
                    elif self.board[Vcur - 1][Hcur - 1] not in [" ", le]:
                        point -= 0.25
                    Vcur = Vpos +(i+5)*step[0]
                    Hcur = Hpos +(i+5)*step[1]
                    if Vcur < 1 or Vcur > self.size or Hcur < 1 or Hcur > self.size:
                        point -= 0.25
                    elif self.board[Vcur - 1][Hcur - 1] not in [' ', le]:
                        point -= 0.25

                    if point > maxpoint:
                        maxpoint = point
                points.append(maxpoint)
            points.sort(reverse=True)
        return points


    def higherScore(self, points1, points2):
        points = []
        counter1 = 0
        counter2 = 0
        while counter1 + counter2 < 4:
            if points1[counter1] >= points2[counter2]:
                points.append(points1[counter1])
                counter1 +=1
            else:
                points.append(points2[counter2])
                counter2 +=1
        return points

    def betterScore(self, points1, points2):
        for i in range(len(points1)):
            if points1[i] > points2[i]:
                return points1
            elif points1[i] < points2[i]:
                return points2
        return points1


    def isBoardFull(self):
        sum = 0
        for i in range(self.size):
            sum += self.board[i].count(' ')
        if sum > 1:
            return False
        else:
            return True



    # Define a random selection
    def selectRandom(self, List):
        ln = len(List)
        r = random.randrange(0, ln)
        return List[r][0], List[r][1]


class player(Comp):
    def __init__(self, N):
        Comp.__init__(self, N)
        self.x = 0
        self.y = 9
        self.imgloc = curdir + "/Image/Tho.jpeg"
        self.name = 'Tho'
        self.age = 21
        self.level = 1920
        self.intro = []

    def compMove(self, other, surface, pos):
        block_size = tools.play_size//self.size
        choose = False
        while not choose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if self.y > 0:
                            self.y -= 1
                    elif event.key == pygame.K_DOWN:
                        if self.y < self.size-1:
                            self.y += 1
                    elif event.key == pygame.K_LEFT:
                        if self.x > 0:
                            self.x -= 1
                    elif event.key == pygame.K_RIGHT:
                        if self.x < self.size-1:
                            self.x += 1
                    elif event.key == pygame.K_SPACE:
                        if self.spaceIsFree(self.x+1, self.y+1):
                            choose = True
                        else:
                            tools.draw_status('Tho chon vi tri khac nhe!', (0, 0, 0), surface)
            tools.draw_play_window(surface, self)
            if pos == 1:
                tools.draw_player1(self, surface)
                tools.draw_player2(other, surface)
            elif pos == 2:
                tools.draw_player2(self, surface)
                tools.draw_player1(other, surface)
            tools.draw_status('!!! Luot danh nay cua '+ self.name, (0, 0, 0), surface)
            pygame.draw.rect(surface, (0, 255, 255), (tools.top_left_x + block_size * self.x,
                                                      tools.top_left_y + block_size * self.y, block_size, block_size), 5)
            pygame.display.update()
        return [self.x+1, self.y+1]


class Comp1(Comp):
    def __init__(self, N):
        Comp.__init__(self, N)
        self.name = 'Gau Trang'
        self.imgloc = curdir + '/Image/GauTrang.jpeg'
        self.age = 22
        self.level = 2
        self.intro = ["Gau Trang Bac Cuc ua thich loi choi phong thu",
                      "va thuong lua chon phuong an phong thu toi uu nhat",
                      "Tuy nhien, neu Tho de ban Gau Trang co co hoi",
                      "de ket thuc van dau se rat nguy hiem day nhe"]


    # Move of computer
    def compMove(self, other, surface, pos):
        max = 0
        maxList = []
        for i in range(self.size):
            for j in range(self.size):
                if self.spaceIsFree(i+1, j+1):
                    if pos == 1:
                        if self.playerpoint('X', i+1, j+1)[0] >= 4:
                            return [i+1, j+1]
                        else:
                            P = self.playerpoint('O', i+1, j+1)[0]
                            if P > max:
                                maxList = [[i+1, j+1]]
                                max = P
                            elif P == max:
                                maxList.append([i+1, j+1])
                    else:
                        if self.playerpoint('O', i+1, j+1)[0] >= 4:
                            return [i+1, j+1]
                        else:
                            P = self.playerpoint('X', i+1, j+1)[0]
                            if P > max:
                                maxList = [[i+1, j+1]]
                                max = P
                            elif P == max:
                                maxList.append([i+1, j+1])
        print(max)
        return self.selectRandom(maxList)


class Comp2(Comp):

    def __init__(self, N):
        Comp.__init__(self, N)
        self.name = 'Canh Cut'
        self.imgloc = curdir + '/Image/CanhCut.jpeg'
        self.age = 1
        self.level = 3
        self.intro = ["Chim Canh Cut co cai nhin tong quat ve the tran,",
                      "va co nhung nuoc di can bang giua tan cong va phong thu.",
                      "Ban Tho hay de y nhung nuoc di cua Chim Canh Cut",
                      "de chan dung y dinh tan cong cua Cut nhe!"]


    def compMove(self,other,  surface, pos):
        # She know how to balance between attack and defense
        max = 0
        maxList = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    Wp = self.higherScore(self.playerpoint('X', i + 1, j + 1),
                                          self.playerpoint('O', i + 1, j + 1))[0]
                    if Wp > max:
                        maxList = []
                        maxList = [[i + 1, j + 1]]
                        max = Wp
                    elif Wp == max:
                        maxList.append([i + 1, j + 1])
        return self.selectRandom(maxList)


class Comp3(Comp):

    def __init__(self, N):
        Comp.__init__(self, N)
        self.name = 'Master Panda'
        self.imgloc = curdir + '/Image/Panda.jpeg'
        self.age = 21
        self.level = 4
        self.intro = ["Gau Panda la bac thay trong bo mon co XO.",
                      " Neu muon tro thanh nguoi so mot trong tro choi nay, ban Tho",
                      "chac chan phai danh bai duoc gau Panda.",
                      "Panda duoc thua huong tri thong minh tu Thuong De",
                      "(Nguoi Sang Lap Tro Choi ^^)."]


    def compMove(self, other, surface, pos):
        # The Master of this game
        max = [0, 0, 0, 0]
        maxList = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == " ":
                    Wp = self.higherScore(self.playerpoint('X', i + 1, j + 1),
                                          self.playerpoint('O', i + 1, j + 1))
                    if self.betterScore(Wp, max) != max:
                        maxList = []
                        maxList = [[i + 1, j + 1]]
                        max = Wp
                    elif Wp == max:
                        maxList.append([i + 1, j + 1])
        return self.selectRandom(maxList)


class Comp4(Comp):

    def __init__(self, N):
        Comp.__init__(self, N)
        self.name = 'Budori'
        self.imgloc = curdir + '/Image/Meo.jpeg'
        self.age = 18
        self.level = 5
        self.intro = []

    def compMove(self, other, surface, pos):
        return self.selectRandom([(i,j) for i in range(self.size) for j in range(self.size) if self.spaceIsFree(i,j)])