import numpy as np
import re
import pickle



class FLIP_DOT_DISPLAY():

    def __init__(self) -> None:
        self.on="\U0001F7E1"
        self.off="\U000026AB"
        self.filename="board.pkl"
        self.board = np.zeros((8, 8))
        
    def flip_a_dot(self, coords: np.ndarray) -> None:
        self.board[coords[0], coords[1]] = (self.board[coords[0], coords[1]] + 1) % 2  #flip the dot
        
    def get_board(self) -> np.ndarray:
        return self.board
    
    def __repr__(self) -> str:
        print(type(self.board))
        output_String = np.array2string(self.board, formatter={'float':lambda x: self.on if x else self.off})

        return " "+ re.sub('[\[\]]', '', output_String)
    
    
    def save_board(self) -> None:
        pickle.dump(self.board, open(self.filename, "wb"))
        
    def load_board(self) -> None:
        self.board=pickle.load(open(self.filename, "rb"))
        
        
board=FLIP_DOT_DISPLAY()
#board.flip_a_dot(np.array([0,0]))
print(board)
#board.save_board()
board.load_board()
board.flip_a_dot([5,5])
print(board)
board.save_board()
