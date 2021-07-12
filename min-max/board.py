import math

class Board:
    def __init__(self):
        self.board = [[' ', ' ', ' '],
                      [' ', ' ', ' '], 
                      [' ', ' ', ' ']]
    
    # check if board is full
    def full(self):
        for arr in self.board:
            for item in arr:
                if item == ' ':
                    return False
        return True

    # check if someone won
    def won(self):
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return True
        if self.board[1][0] != ' ' and self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return True
        if self.board[2][0] != ' ' and self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return True
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return True
        if self.board[0][1] != ' ' and self.board[0][1] == self.board[1][1]  == self.board[2][1]:
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return True
        if self.board[0][0] != ' ' and self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != ' ' and self.board[0][2] == self.board[1][1] ==  self.board[2][0]:
            return True
        return False

    # prints the board
    def print(self):
        print("-------------")
        print("|", self.board[0][0], "|", self.board[0][1], "|", self.board[0][2], "|")
        print("|", self.board[1][0], "|", self.board[1][1], "|", self.board[1][2], "|")
        print("|", self.board[2][0], "|", self.board[2][1], "|", self.board[2][2], "|")
        print("-------------")


# represents a move in tic tac toe
class Move:
    def __init__(self, val, i = None, j = None):
        self.val = val
        self.i = i
        self.j = j


# translates the number the user picks to a slot on the board
def make_move(game, postition): 
    if postition == '0' and game.board[0][0] == ' ':
        game.board[0][0] = 'X'
        return True
    if postition == '1' and game.board[0][1] == ' ':
        game.board[0][1] = 'X'
        return True
    if postition == '2' and game.board[0][2] == ' ':
        game.board[0][2] = 'X'
        return True
    if postition == '3' and game.board[1][0] == ' ':
        game.board[1][0] = 'X'
        return True
    if postition == '4' and game.board[1][1] == ' ':
        game.board[1][1] = 'X'
        return True
    if postition == '5' and game.board[1][2] == ' ':
        game.board[1][2] = 'X'
        return True
    if postition == '6' and game.board[2][0] == ' ':
        game.board[2][0] = 'X'
        return True
    if postition == '7' and game.board[2][1] == ' ':
        game.board[2][1] = 'X'
        return True
    if postition == '8' and game.board[2][2] == ' ':
        game.board[2][2] = 'X'
        return True
    return False


# prints the board with the numbering system used for user input
def print_info_board():
    info = Board()
    info.board[0][0] = '0'
    info.board[0][1] = '1'
    info.board[0][2] = '2'
    info.board[1][0] = '3'
    info.board[1][1] = '4'
    info.board[1][2] = '5'
    info.board[2][0] = '6'
    info.board[2][1] = '7'
    info.board[2][2] = '8'
    info.print() 


# gets score for static state of game
# 1 is score for bot win, -1 is score for human win, 0 is score for no win
def get_score(game): 
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[0][1] == game.board[0][2]:
        if game.board[0][0] == 'O':
            return 1
        return -1
    if game.board[1][0] != ' ' and game.board[1][0] == game.board[1][1] == game.board[1][2]:
        if game.board[1][0] == 'O':
            return 1
        return -1
    if game.board[2][0] != ' ' and game.board[2][0] == game.board[2][1] == game.board[2][2]:
        if game.board[2][0] == 'O':
            return 1
        return -1
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[1][0] == game.board[2][0]:
        if game.board[0][0] == 'O':
            return 1
        return -1
    if game.board[0][1] != ' ' and game.board[0][1] == game.board[1][1] == game.board[2][1]:
        if game.board[0][1] == 'O':
            return 1
        return -1
    if game.board[0][2] != ' ' and game.board[0][2] == game.board[1][2] == game.board[2][2]:
        if game.board[0][2] == 'O':
            return 1
        return -1
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[1][1] == game.board[2][2]:
        if game.board[0][0] == 'O':
            return 1
        return -1
    if game.board[0][2] != ' ' and game.board[0][2] == game.board[1][1] == game.board[2][0]:
        if game.board[0][2] == 'O':
            return 1
        return -1
    return 0


# gets the winnder of the game
def get_winner(game):
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[0][1] == game.board[0][2]:
        return game.board[0][0]
    if game.board[1][0] != ' ' and game.board[1][0] == game.board[1][1] == game.board[1][2]:
        return game.board[1][0]
    if game.board[2][0] != ' ' and game.board[2][0] == game.board[2][1] == game.board[2][2]:
        return game.board[2][0]
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[1][0] == game.board[2][0]:
        return game.board[0][0]
    if game.board[0][1] != ' ' and game.board[0][1] == game.board[1][1] == game.board[2][1]:
        return game.board[0][1]
    if game.board[0][2] != ' ' and game.board[0][2] == game.board[1][2] == game.board[2][2]:
        return game.board[0][2]
    if game.board[0][0] != ' ' and game.board[0][0] == game.board[1][1] == game.board[2][2]:
        return game.board[0][0]
    if game.board[0][2] != ' ' and game.board[0][2] == game.board[1][1] == game.board[2][0]:
        return game.board[0][2]
    return "No one"