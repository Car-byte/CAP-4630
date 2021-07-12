from board import Move
from board import Board
from board import print_info_board
from board import make_move
from board import get_score
from board import get_winner
import math


# min max algorithm with alpha beta prunning
def minmax_alphabeta(game, depth, maxturn, alpha = -math.inf, beta = math.inf):
    if depth == 0 or game.full() or game.won(): # if game is over or max depth is reached
        return Move(get_score(game))
    terminate_loop = False
    if maxturn:
        eval = Move(-math.inf)
        for i in range(len(game.board)):
            for j in range(len(game.board[i])): # loop through all points in the game
                if game.board[i][j] == ' ': # try O on all empty spaces
                    game.board[i][j] = 'O'
                    temp = minmax_alphabeta(game, depth - 1, False, alpha, beta) # call recursivly to expand tree
                    game.board[i][j] = ' '
                    if temp.val > eval.val: # if this decision is better than the previous ones
                        eval.val = temp.val
                        eval.i = i
                        eval.j = j
                    alpha = max(alpha, eval.val) # update alpha
                    if beta <= alpha: # if going farther down the tree cannot change our outcome, return
                        terminate_loop = True
                        break
                if terminate_loop: # we need this type of condition for breaking double loop in python because updating i and j does not work
                    break
        return eval
    else:
        eval = Move(math.inf) # same comments as above just with X and O replaced
        for i in range(len(game.board)):
            for j in range(len(game.board[i])):
                if game.board[i][j] == ' ':
                    game.board[i][j] = 'X'
                    temp = minmax_alphabeta(game, depth - 1, True, alpha, beta)
                    game.board[i][j] = ' '
                    if temp.val < eval.val:
                        eval.val = temp.val
                        eval.i = i
                        eval.j = j
                    beta = min(beta, eval.val)
                    if beta <= alpha:
                        terminate_loop = True
                if terminate_loop:
                    break
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
        minmax_move = minmax_alphabeta(game, math.inf, True)
        game.board[minmax_move.i][minmax_move.j] = 'O'
    game.print()
    winner = get_winner(game)
    if winner == "O":
        winner = "Bot"
    elif winner == "X":
        winner = "Human"
    print(winner, "Wins")
