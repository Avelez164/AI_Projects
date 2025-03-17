from games import *
from utils import *

class GameOfNim(Game):
    def __init__(self, board=[3,1]):
        moves = [(x,y) for x in range(0, len(board))
                 for y in range(1,(board[x] + 1))]
        self.initial = GameState(to_move='MAX', utility=0, board=board, moves=moves)

    def actions(self, state):
        return state.moves
    
    def result(self, state, move):
        if move not in state.moves:
            return state
        board = state.board.copy()
        board[move[0]] = board[move[0]] - move[1]
        moves = [(x,y) for x in range(0, len(board))
                 for y in range(1,(board[x] + 1))]
        utility = self.compute_utility(board, state.to_move)
        return GameState(to_move=('MIN' if state.to_move == 'MAX' else 'MAX'),
                         utility=utility,
                         board=board, moves=moves)
    
    def utility(self, state, player):
        return state.utility if player == 'MAX' else -state.utility
    
    def terminal_test(self, state):
        return len(state.moves) == 0

    def display(self, state):
        board = state.board
        print("board:", board)
    
    def compute_utility(self, board, player):
        if all(x == 0 for x in board):
            return +1 if player == 'MAX' else -1
        elif len([(x,y) for x in range(0, len(board)) for y in range(1,(board[x] + 1))]) == 0:
            return -1 if player == 'MAX' else +1
        else:
            return 0
        
    def check_all_zeros(self, board):
        return all(x == 0 for x in board)


if __name__ == "__main__":
    nim = GameOfNim(board=[0,5,3,1])
    nim = GameOfNim(board=[7,5,3,1])
    print(nim.initial.board)
    print(nim.initial.moves)
    print(nim.result(nim.initial, (1,2)))
    utility = nim.play_game(alpha_beta_player, query_player)
    if (utility < 0):
        print("MIN Wins!")
    else:
        print("MAX Wins!")
