"""
Tic Tac Toe Player
"""

import math
import copy
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_x=0
    count_o=0
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                continue
            elif board[i][j]==X:
                count_x+=1
            else:
                count_o+=1

    if count_x==count_o:
        return X
    else:
        return O
    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #creating set for tuples
    moves=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                moves.add((i,j))
    return moves
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board=copy.deepcopy(board)
    if action  not in actions(new_board):
        raise ValueError("Invalid positioning")
    
    next_move=player(new_board)
    i,j=action
    new_board[i][j]=next_move

    return new_board
    raise NotImplementedError



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0]==board[1][1]==board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    elif board[2][0]==board[1][1]==board[0][2] and board [1][1] is not EMPTY:
        return board[1][1]

    for i in range(3):
            if board[i][0]==board[i][1]==board[i][2] and board[i][0] is not EMPTY:
                return board [i][0]
            elif board[0][i]==board[1][i]==board[2][i] and board[0][i] is not EMPTY:
                return board[0][i]
    return None   
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    else:
        if len(actions(board))==0 :
            return True
    return False
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)
    if result==X:
        return 1
    elif result==O:
        return -1
    else:
        return 0
    raise NotImplementedError

def max_val(board):
    if terminal(board):
        return utility(board)
    
    v=float("-inf")
    for i in actions(board):
        v=max(v,min_val(result(board,i)))

    return v
def min_val(board):
    if terminal(board):
        return utility(board)
    
    v=float("inf")
    for i in actions(board):
        v=min(v,max_val(result(board,i)))

    return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    res=player(board)
    best_move=None

    if res==X:
        x=float("-inf")
        for i in actions(board):
            val=min_val(result(board,i))
            if val>x:
                x=val
                best_move=i
    else:
        x=float("inf")
        for i in actions(board):
            val=max_val(result(board,i))
            if val<x:
                x=val
                best_move=i
    return best_move

    raise NotImplementedError
