import pygame
import Player
import inputbox
import ImgModify

pygame.font.init()

# There would be two play modes board 10x10 or 15x15

# Global variables
s_width = 1200
s_height = 800
play_size = 450

top_left_x = (s_width - play_size) // 2
top_left_y = (s_height - play_size) // 2

def draw_player_list(surface):
    player1 = Player.player(1)
    player2 = Player.Comp1(1)
    player3 = Player.Comp2(1)
    player4 = Player.Comp3(1)
    player5 = Player.Comp4(1)
    PlayerList = [player1, player2, player3, player4, player5]
    surface.fill((0,0,0))
    fontnumber = pygame.font.SysFont('conmiscans', 60)
    fontname = pygame.font.SysFont('conmiscans', 40)
    draw_text_middle('Chon Nguoi Choi', 50, (255,0,0), -70, surface)
    for i in range(len(PlayerList)):
        numberlabel = fontnumber.render(str(i+1), True, (255, 255, 255))
        namelabel = fontname.render(PlayerList[i].name, True, (255, 255, 255))
        image = pygame.image.load(PlayerList[i].imgloc)
        surface.blit(numberlabel, (i*s_width//5+(s_width//5-numberlabel.get_width())//2, 150))
        surface.blit(image, (i*s_width//5+(s_width//5-image.get_width())//2, 155 + numberlabel.get_height()))
        surface.blit(namelabel,(i*s_width//5+(s_width//5-namelabel.get_width())//2,
                                 160+numberlabel.get_height()+image.get_height()))
        pygame.draw.rect(surface, (255,255,0), (i*s_width//5+(s_width//5-image.get_width())//2, 155+numberlabel.get_height(),
                                                image.get_width(), image.get_height()),5)
    draw_status('!!!Nhan cac so tuong ung de chon nguoi choi', (255,255,255), surface)
    pygame.display.update()

def draw_text_middle(text, size, color, depth, surface):
    font = pygame.font.SysFont('comicsans', size, bold=True)
    label = font.render(text, True, color)
    surface.blit(label, (top_left_x + play_size//2 - (label.get_width()//2),
                         top_left_y + depth - label.get_height()/2))

def draw_status(text, color, surface):
    font = pygame.font.SysFont('chalkduster', 40)
    label = font.render(text, True, color)
    surface.blit(label, ((s_width-label.get_width())//2, s_height - label.get_height() - 10 ))

def draw_grid(surface, size):
    sx = top_left_x
    sy = top_left_y
    block_size = play_size//size
    for i in range(size):
        pygame.draw.line(surface, (128, 128, 128), (sx, sy + i * block_size),
                         (sx + play_size, sy + i * block_size))  # horizontal line
        for j in range(size):
            pygame.draw.line(surface, (128, 128, 128), (sx + j * block_size, sy),
                             (sx + j * block_size, sy + play_size))  # vertical line


def draw_player1(player, surface):
    fontname = pygame.font.SysFont('comicsans', 40)
    namelabel = fontname.render(player.name, True, (0, 0, 255))
    sx1 = top_left_x - 150 - namelabel.get_width()//2
    sy1 = top_left_y + play_size // 2 - 150
    surface.blit(namelabel, (sx1, sy1))
    image = pygame.image.load(player.imgloc)
    sx2 = sx1 + (namelabel.get_width()-image.get_width())//2
    sy2 = sy1 + namelabel.get_height() + 10
    surface.blit(image, (sx2, sy2))
    pygame.draw.rect(surface, ( 0, 0, 255), (sx2, sy2, image.get_width(), image.get_height()),5)


def draw_player2(player, surface):
    fontname = pygame.font.SysFont('comicsans', 40)
    namelabel = fontname.render(player.name, True, (255, 0, 0))
    sx1 = top_left_x + play_size + 150 - namelabel.get_width()//2
    sy1 = top_left_y + play_size // 2 - 150
    surface.blit(namelabel, (sx1, sy1))
    image = pygame.image.load(player.imgloc)
    sx2 = sx1 + (namelabel.get_width()-image.get_width())//2
    sy2 = sy1 + namelabel.get_height() + 10
    surface.blit(image, (sx2, sy2))
    pygame.draw.rect(surface, (255, 0, 0), (sx2, sy2, image.get_width(), image.get_height()),5)


def draw_icon(Icon, surface):
    sx = top_left_x + play_size + 60
    sy = top_left_y + play_size / 2 + 50
    fontname = pygame.font.SysFont('comicsans', 40)
    scriptlabel = fontname.render(Icon.script, True, (255, 0, 0))
    image = pygame.image.load(Icon.imgloc)
    surface.blit(scriptlabel, (sx+(image.get_width()-scriptlabel.get_width())//2,
                               sy-scriptlabel.get_height()-5))
    surface.bilt(image, (sx, sy))


def draw_play_window(surface, player):
    block_size = play_size//player.size
    surface.fill((255, 255, 255))
    # Game Title
    titlefont = pygame.font.SysFont('comicsans', 60)
    titlelabel = titlefont.render('Tro Choi XO', True, (0, 0, 0))
    surface.blit(titlelabel, (top_left_x + play_size / 2 - (titlelabel.get_width() / 2), 15))
    signfont = pygame.font.SysFont('comiscans', (block_size*3)//4, True)
    for i in range(player.size):
        for j in range(player.size):
            if player.board[i][j] == "X":
                signlabel = signfont.render(player.board[i][j], True, (0, 0, 255))
                surface.blit(signlabel, (top_left_x + i * block_size + (block_size-signlabel.get_width())//2,
                                         top_left_y + j * block_size + (block_size-signlabel.get_height())//2))
            elif player.board[i][j] == "O":
                signlabel = signfont.render(player.board[i][j], True, (255, 0, 0))
                surface.blit(signlabel, (top_left_x + i * block_size + (block_size - signlabel.get_width()) // 2,
                                         top_left_y + j * block_size + (block_size - signlabel.get_height()) // 2))
    # draw grid and border
    draw_grid(surface, player.size)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_size, play_size), 5)
    # pygame.display.update()


def draw_winner(winner, surface):
    font = pygame.font.SysFont('comicsans', 40)
    if winner is not None:
        label = font.render('Chuc mung ' + winner.name + ' da gianh chien thang!', True, (255, 0, 0))
    else:
        label = font.render('Hoa roi minh cung choi lai nhe!', True, (255, 0, 0))
    surface.fill((0, 0, 0))
    Img = ImgModify.getImgColor('Champion.jpeg', 160, 160)
    for i in range(len(Img)):
        for j in range(len(Img[i])):
            pygame.draw.rect(surface, Img[i][j], ((s_width-s_height)//2 + j*s_height//len(Img[i]),
                                                  i*s_height//len(Img[i]), s_height//len(Img[i]), s_height//len(Img[i])))
    surface.blit(label, ((s_width - label.get_width()) // 2, 20))
    pygame.display.update()


IconList = []


def match(win, player1, player2):
    # player 1 take the first turn
    playerturn = 0
    hasWinner = False
    while not hasWinner:
        if playerturn%2 == 0:
            [moveV, moveH] = player1.compMove(player2, win, 1)
            player1.insertLetter(player2, 'X', moveV, moveH)
            if player1.playerpoint('X', moveV, moveH)[0] >= 4.5:
                hasWinner = True
        else:
            [moveV, moveH] = player2.compMove(player1, win, 2)
            player2.insertLetter(player1, 'O', moveV, moveH)
            if player2.playerpoint('O', moveV, moveH)[0] >= 4.5:
                hasWinner = True
        draw_play_window(win, player1)
        #draw_icon()
        if playerturn%2 == 0:
            draw_status('!!!' + player1.name + ' vua dien X vao vi tri ({0}, {1})'.format(moveV, moveH), (0, 0, 0), win)
        else:
            draw_status('!!!' + player2.name + ' vua dien O vao vi tri ({0}, {1})'.format(moveV, moveH), (0, 0, 0), win)
        draw_player1(player1, win)
        draw_player2(player2, win)
        pygame.display.update()
        pygame.time.delay(2000)
        if hasWinner:
            if playerturn%2 == 0:
                return player1
            else:
                return player2
        elif player1.isBoardFull():
            return None
        playerturn +=1


IntroList = ["Ban Tho hay an mot nut bat ky",
             "Ngay xua ngay xua",
             "Co mot vuong quoc nam rat xa the gioi loai nguoi",
             "Tai day, nhung loai dong vat de thuong chung song cung nhau",
             "Dong vat trong the gioi nay so huu nhung tri tue vuot troi",
             "Nguoi ta truyen tai nhau rang",
             "Tri tue nay den tu mot tro choi co truyen trong vuong quoc",
             "Do la ... Tro choi XO",
             "Trong tro choi nguoi choi phai tim cach tao ra",
             "mot duong thang co do dai bang 5 truoc doi phuong",
             "de danh chien thang",
             "Chien thang moi van choi se lam tang chi so thong minh",
             "Tho hay tham gia cung cac ban de tro thanh",
             "Nguoi thong minh nhat vuong quoc nhe",
             "Dau tien ta hay chon kich thuoc cua ban thi dau",
             "Nhan (N) de chon bang nho     Nhan (L) de chon bang lon",
             "Hay san sang cho tran thi dau nao"]


def intro(win):
    # Intro
    counter = 0
    while counter < len(IntroList) - 2:
        win.fill((0, 0, 0))
        draw_text_middle(IntroList[counter], 35, (255, 255, 255), 100 ,win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                counter += 1
    # Choose board size
    chooseboard = False
    boardsize = 10
    while not chooseboard:
        win.fill((0, 0, 0))
        draw_text_middle(IntroList[counter], 35, (255, 255, 255), 100, win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_n:
                    boardsize = 10
                    chooseboard = True
                    counter += 1
                elif event.key == pygame.K_l:
                    boardsize = 15
                    chooseboard = True
                    counter += 1

    # Choose players
    playernumber = 0
    players = []
    draw_player_list(win)
    while playernumber < 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    players.append(Player.player(boardsize))
                    playernumber += 1
                elif event.key == pygame.K_2:
                    players.append(Player.Comp1(boardsize))
                    playernumber += 1
                elif event.key == pygame.K_3:
                    players.append(Player.Comp2(boardsize))
                    playernumber += 1
                elif event.key == pygame.K_4:
                    players.append(Player.Comp3(boardsize))
                    playernumber += 1
                elif event.key == pygame.K_5:
                    players.append(Player.Comp4(boardsize))
                    playernumber += 1
        for i in range(playernumber):
            draw_text_middle("Nguoi choi thu {0}: ".format(i+1)+players[i].name, 30, (255, 255, 255), 200+40+i*40, win)
            pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                run = False

    for player in players:
        if player.name == 'Tho':
            player.name = inputbox.draw_input_window(win,'Hay dien ten cua Tho:', 700, 300)

    playercounter = 0
    while playercounter < 2:
            Information = ["Nguoi choi: "+players[playercounter].name,
                           "Tuoi : {0}".format(players[playercounter].age),
                           "Level :" + str(players[playercounter].level)] + players[playercounter].intro
            win.fill((0,0,0))
            playerimage = pygame.image.load(players[playercounter].imgloc)
            win.blit(playerimage, (s_width//2-playerimage.get_width()//2, 100))
            pygame.draw.rect(win, (255,255,0), (s_width//2-playerimage.get_width()//2, 100,
                                                playerimage.get_width(), playerimage.get_height()),5)
            pygame.display.update()
            inforcounter = 0
            while inforcounter < len(Information):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        draw_text_middle(Information[inforcounter], 30, (255, 255, 255),
                                         20 + playerimage.get_height() + inforcounter * 30, win)
                        pygame.display.update()
                        inforcounter += 1
            run = True
            while run:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                    if event.type == pygame.KEYDOWN:
                        playercounter += 1
                        run = False


    while counter < len(IntroList):
        win.fill((0, 0, 0))
        draw_text_middle(IntroList[counter], 35, (255, 255, 255), 100, win)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                counter += 1
    return players[0], players[1]


def end_game(win, winner):
    draw_winner(winner, win)
    pygame.time.delay(8000)
    pass

def main_menu(win):
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                player1, player2 = intro(win)
                winner = match(win, player1, player2)
                end_game(win, winner)



def main_process():
    win = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('XO CUNG THO')
    main_menu(win)
