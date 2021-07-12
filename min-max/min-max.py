from board import Move
from board import Board
from board import print_info_board
from board import make_move
from board import get_score
from board import get_winner
import math

# the min max algorithm
def minmax(game, depth, maxturn):
    if depth == 0 or game.full() or game.won(): # if game is over or max depth is reached
        return Move(get_score(game))

    if maxturn: # bots turn
        eval = Move(-math.inf)
        for i in range(len(game.board)):
            for j in range(len(game.board[i])): # loop through all points in the game
                if game.board[i][j] == ' ': # try O on all empty spaces
                    game.board[i][j] = 'O' # we replace the current board so we do not need to make a copy
                    temp = minmax(game, depth - 1, False) # call recursivly to expand tree
                    game.board[i][j] = ' ' # return board to previous state
                    if temp.val > eval.val: # if this decision is better than the previous ones
                        eval.val = temp.val
                        eval.i = i
                        eval.j = j
        return eval
    else: # human turn
        eval = Move(math.inf)
        for i in range(len(game.board)):
            for j in range(len(game.board[i])):
                if game.board[i][j] == ' ':
                    game.board[i][j] = 'X'
                    temp = minmax(game, depth - 1, True)
                    game.board[i][j] = ' '
                    if temp.val < eval.val:
                        eval.val = temp.val
                        eval.i = i
                        eval.j = j
        return eval



if __name__ == "__main__":
    print_info_board()
    game = Board()
    while not game.full() and not game.won():
        game.print()
        position = input("Where would you like to go (0-8)?: ")
        position = position.strip()
        while not make_move(game, position):
            position = input("Not a vlid position please enter a valid position 0-8 from left to right: ")
            position = position.strip()
        game.print()
        if game.won() or game.full():
            break
        minmax_move = None
        minmax_move = minmax(game, math.inf, True)
        game.board[minmax_move.i][minmax_move.j] = 'O'
    game.print()
    winner = get_winner(game)
    if winner == "O":
        winner = "Bot"
    elif winner == "X":
        winner = "Human"
    print(winner, "Wins")
