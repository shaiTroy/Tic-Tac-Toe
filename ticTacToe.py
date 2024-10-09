from typing import List
from os import system, name
from time import sleep
import random
import pygame, sys


def actions(game: List[int]) -> List[List[int]]:
    possible_actions = []
    for i in range(3):
        for j in range(3):
            if game[i][j] == 1:
                possible_actions.append((i, j))
    return possible_actions

def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


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

def changeSpot(game: List[int], row: int, col: int, player: str):
    if game[row][col] == 1:
        game[row][col] = player
    else:
        print("Spot is already taken. Please try again.")
        get_valid_coordinate(game, player)
    return
    

def get_valid_coordinate(game: List[int], player: str):
    while True:
        row = int(input("Enter the row coordinate (0-2): "))
        col = int(input("Enter the column coordinate (0-2): "))
        if 0 <= row <= 2 and 0 <= col <= 2:
            changeSpot(game, row, col, player)
            return
        else:
            print("Invalid coordinate. Please try again.")
            
def printGame(game: List[int]):
    for line in game:
        for i in range(len(line)):
            if line[i] == 1:
                print("_", end=" ")
            else:
                print(line[i], end=" ")
        print()
        
def first(game: List[int]):
    while True:
        clear()
        printGame(game)
        get_valid_coordinate(game, "X")
        if terminal(game):
            winner = checkWin(game)
            clear()
            if winner == 1:
                printGame(game)
                print("Computer wins!")
            elif winner == -1:
                printGame(game)
                print("You win!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        
        clear()
        _, game = minimax(game, "O")
        if terminal(game):
            clear()
            winner = checkWin(game)
            if winner == 1:
                printGame(game)
                print("Computer wins!")
            elif winner == -1:
                printGame(game)
                print("You win!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        

def second(game: List[int]):
    randomStart = random.randrange(0, 8)
    starts = actions(game)
    for index, value in enumerate(starts):
        if index == randomStart:
            game = result(game, value, "X")
            break
    
    while True:
        clear()
        printGame(game)
        get_valid_coordinate(game, "O")
        if terminal(game):
            winner = checkWin(game)
            clear()
            if winner == -1:
                printGame(game)
                print("Computer wins!")
            elif winner == 1:
                printGame(game)
                print("You win!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        
        clear()
        _, game = minimax(game, "X")
        if terminal(game):
            clear()
            winner = checkWin(game)
            if winner == -1:
                printGame(game)
                print("Computer wins!")
            elif winner == 1:
                printGame(game)
                print("You win!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        
def third(game: List[int]):
    randomStart = random.randrange(0, 8)
    starts = actions(game)
    for index, value in enumerate(starts):
        if index == randomStart:
            game = result(game, value, "X")
            break
        
    while True:
        clear()
        printGame(game)
        sleep(1)
        _, game = minimax(game, "O")
        if terminal(game):
            winner = checkWin(game)
            clear()
            if winner == 1:
                printGame(game)
                print("X wins!")
            elif winner == -1:
                printGame(game)
                print("O wins!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        
        clear()
        printGame(game)
        sleep(1)
        _, game = minimax(game, "X")
        if terminal(game):
            clear()
            winner = checkWin(game)
            if winner == 1:
                printGame(game)
                print("X wins!")
            elif winner == -1:
                printGame(game)
                print("O wins!")
            else:
                printGame(game)
                print("It's a tie!")
            sleep(4)
            return
        
    
    

def main():
    while True:
        clear()
        print("Welcome to Tic Tac Toe!")
        print("1. Start against computer")
        print("2. Play second against computer")
        print("3. Have computer play another computer")
        print("4. Exit")
    
        game = [[1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]]
    
        option = int(input("Enter your choice (1-4): "))
        
        if option == 1:
            # Option 1: Start against computer
            print("You chose to start against the computer.")
            first(game)
            
            
        elif option == 2:
            # Option 2: Play second against computer
            print("You chose to play second against the computer.")
            second(game)
            
            
        elif option == 3:
            # Option 3: Have computer play another computer
            print("You chose to have the computer play against itself.")
            third(game)                
            
        elif option == 4:
            # Option 4: Exit
            print("Exiting the game. Goodbye!")
            break
        
        else:
            print("Invalid option. Please try again.")
main()