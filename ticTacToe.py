from typing import List
from os import system, name
from time import sleep
from button import Button
import random
import pygame, sys
 
pygame.init()
 
WIDTH, HEIGHT = 900, 900
 
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe!")

BOARD = pygame.image.load("assets/Board.png")
X_IMG = pygame.image.load("assets/X.png")
O_IMG = pygame.image.load("assets/O.png")
BUTTON = pygame.image.load("assets/Button.png")

BG_COLOR = (214, 201, 227)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def render_board(board, ximg, oimg, graphical_board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                graphical_board[i][j][0] = ximg
                graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
            elif board[i][j] == 'O':
                graphical_board[i][j][0] = oimg
                graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))
    for i in range(3):
        for j in range(3):
            if graphical_board[i][j][0] is not None:
                SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])

def actions(game: List[int]) -> List[List[int]]:
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if game[i][j] == 1:
                possible_actions.append((i, j))
    return possible_actions

def result(game: List[int], action: List[int], player: str):
    game_copy = [row.copy() for row in game]
    game_copy[action[0]][action[1]] = player
    return game_copy

def minimax(game: List[int], player: str):
    if terminal(game):
        return checkWin(game), game
    if player == "X":
        best_value = (1000, None)
        for action in actions(game):
            movement = result(game, action, player)
            value, _ = minimax(movement, "O")
            if value < best_value[0]:
                best_value = (value, movement)
        return best_value[0], best_value[1]
    else:
        best_value = (-1000, None)
        for action in actions(game):
            movement = result(game, action, player)
            value, _ = minimax(movement, "X")
            if value > best_value[0]:
                best_value = (value, movement)
        return best_value[0], best_value[1]

def terminal(game: List[int]):
    for i in range(3):
        if game[i][0] != 1 and game[i][0] == game[i][1] == game[i][2]: 
            return True
        elif game[0][i] != 1 and game[0][i] == game[1][i] == game[2][i]: 
            return True
    if game[0][0] != 1 and game[0][0] == game[1][1] == game[2][2]: 
            return True
    elif game[0][2] != 1 and game[0][2] == game[1][1] == game[2][0]: 
            return True
    elif not actions(game):
        return True
    return False

def checkWin(game: List[int]):
    for i in range(3):
        if game[i][0] == game[i][1] == game[i][2] and game[i][0] != 1:
            if game[i][0] == "X":
                return -1
            else: return 1
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 1:
            if game[0][i] == "X":
                return -1
            else: return 1
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 1:
        if game[0][0] == "X":
            return -1
        else: return 1
    if game[0][2] == game[1][1] == game[2][0] and game[0][2] != 1:
        if game[1][1] == "X":
            return -1
        else: return 1
    return 0
    
def add_XO(board, graphical_board, to_move,):
    current_pos = pygame.mouse.get_pos()
    converted_x = (current_pos[0]-65)/835*2
    converted_y = current_pos[1]/835*2
    if board[round(converted_y)][round(converted_x)] != 'O' and board[round(converted_y)][round(converted_x)] != 'X':
        board[round(converted_y)][round(converted_x)] = to_move
        if to_move == 'O':
            to_move = 'X'
        else:
            to_move = 'O'
    
    render_board(board, X_IMG, O_IMG, graphical_board)


    return board, to_move      

def first():
    graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
    game = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64, 64))
    render_board(game, X_IMG, O_IMG, graphical_board)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #user turn
            if event.type == pygame.MOUSEBUTTONDOWN:
                game, _ = add_XO(game, graphical_board, "X")
                pygame.display.update()
                if terminal(game):
                    winner = checkWin(game)
                    if winner == 1:
                        Owins(1)
                    elif winner == -1:
                        Xwins(1)
                    else:
                        Tie(1)
                sleep(1)
                #after user goes, computer goes
                _, game = minimax(game, "O")
                render_board(game, X_IMG, O_IMG, graphical_board)
                pygame.display.update()
                if terminal(game):
                    winner = checkWin(game)
                    if winner == 1:
                        Owins(1)
                    elif winner == -1:
                        Xwins(1)
                    else:
                        Tie(1)
           
def second():
    graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
    game = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64, 64))
    randomStart = random.randrange(0, 8)
    starts = actions(game)
    for index, value in enumerate(starts):
        if index == randomStart:
            game = result(game, value, "X")
            break
    render_board(game, X_IMG, O_IMG, graphical_board)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #user turn
            if event.type == pygame.MOUSEBUTTONDOWN:
                game, _ = add_XO(game, graphical_board, "O")
                pygame.display.update()
                if terminal(game):
                    winner = checkWin(game)
                    if winner == -1:
                        Xwins(2)
                    elif winner == 1:
                        Owins(2)
                    else:
                        Tie(2)
                sleep(1)
                #after user goes, computer goes
                _, game = minimax(game, "X")
                render_board(game, X_IMG, O_IMG, graphical_board)
                pygame.display.update()
                if terminal(game):
                    winner = checkWin(game)
                    if winner == -1:
                        Xwins(2)
                    elif winner == 1:
                        Owins(2)
                    else:
                        Tie(2)
        
def third():
    graphical_board = [[[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]], 
                    [[None, None], [None, None], [None, None]]]
    game = [[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]]
    SCREEN.fill(BG_COLOR)
    SCREEN.blit(BOARD, (64, 64))
    randomStart = random.randrange(0, 8)
    starts = actions(game)
    for index, value in enumerate(starts):
        if index == randomStart:
            game = result(game, value, "X")
            break
    render_board(game, X_IMG, O_IMG, graphical_board)
    pygame.display.update()
    while True:
        sleep(1)
        _, game = minimax(game, "O")
        render_board(game, X_IMG, O_IMG, graphical_board)
        pygame.display.update()
        if terminal(game):
            winner = checkWin(game)
            if winner == -1:
                Xwins(3)
            elif winner == 1:
                Owins(3)
            else:
                Tie(3)
        sleep(1)
        _, game = minimax(game, "X")
        render_board(game, X_IMG, O_IMG, graphical_board)
        pygame.display.update()
        if terminal(game):
            winner = checkWin(game)
            if winner == -1:
                Xwins(3)
            elif winner == 1:
                Owins(3)
            else:
                Tie(3)
            
def Xwins(gameNum: int):
    while True:
        XWIN_MOUSE_POS = pygame.mouse.get_pos()
        XWIN_TEXT = get_font(100).render("X WINS", True, "#b68f40")
        XWIN_RECT = XWIN_TEXT.get_rect(center=(460, 100))
        AGAIN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 400), 
                                text_input="PLAY AGAIN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(460, 600), 
                                text_input="MAIN MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(XWIN_TEXT, XWIN_RECT)
        
        for button in [AGAIN_BUTTON, BACK_BUTTON]:
            button.changeColor(XWIN_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AGAIN_BUTTON.checkForInput(XWIN_MOUSE_POS):
                    if gameNum == 1:
                        first()
                    elif gameNum == 2:
                        second()
                    else:
                        third()
                if BACK_BUTTON.checkForInput(XWIN_MOUSE_POS):
                    MainMenu()

        pygame.display.update()
   
def Owins(gameNum: int):
    while True:
        OWIN_MOUSE_POS = pygame.mouse.get_pos()
        OWIN_TEXT = get_font(100).render("O WINS", True, "#b68f40")
        OWIN_RECT = OWIN_TEXT.get_rect(center=(460, 100))
        AGAIN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 400), 
                                text_input="PLAY AGAIN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(460, 600), 
                                text_input="MAIN MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(OWIN_TEXT, OWIN_RECT)
        
        for button in [AGAIN_BUTTON, BACK_BUTTON]:
            button.changeColor(OWIN_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AGAIN_BUTTON.checkForInput(OWIN_MOUSE_POS):
                    if gameNum == 1:
                        first()
                    elif gameNum == 2:
                        second()
                    else:
                        third()
                if BACK_BUTTON.checkForInput(OWIN_MOUSE_POS):
                    MainMenu()

        pygame.display.update()     
              
def Tie(gameNum: int):
    while True:
        TIE_MOUSE_POS = pygame.mouse.get_pos()
        TIE_TEXT = get_font(100).render("TIE", True, "#b68f40")
        TIE_RECT = TIE_TEXT.get_rect(center=(460, 100))
        AGAIN_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 400), 
                                text_input="PLAY AGAIN", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        BACK_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(460, 600), 
                                text_input="MAIN MENU", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        
        SCREEN.blit(TIE_TEXT, TIE_RECT)
        
        for button in [AGAIN_BUTTON, BACK_BUTTON]:
            button.changeColor(TIE_MOUSE_POS)
            button.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if AGAIN_BUTTON.checkForInput(TIE_MOUSE_POS):
                    if gameNum == 1:
                        first()
                    elif gameNum == 2:
                        second()
                    else:
                        third()
                if BACK_BUTTON.checkForInput(TIE_MOUSE_POS):
                    MainMenu()

        pygame.display.update() 

def MainMenu():
    while True:
        SCREEN.fill(BG_COLOR)
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(460, 100))

        FIRST_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(460, 250), 
                            text_input="PLAY FIRST", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        SECOND_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(460, 400), 
                            text_input="PLAY SECOND", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        AIVSAI_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 550), 
                            text_input="AI VS AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(460, 700), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [FIRST_BUTTON, SECOND_BUTTON, AIVSAI_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if FIRST_BUTTON.checkForInput(MENU_MOUSE_POS):
                    first()
                if SECOND_BUTTON.checkForInput(MENU_MOUSE_POS):
                    second()
                if AIVSAI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    third()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
          
MainMenu()