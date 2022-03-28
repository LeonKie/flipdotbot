import numpy as np
import re
import pickle
import os


class FLIP_DOT_DISPLAY():

    def __init__(self) -> None:
        self.on="\U0001F7E1"
        self.off="\U000026AB"
        self.filename="board.pkl"
        self.board = np.zeros((7, 11))
        
    def flip_a_dot(self, coords: np.ndarray) -> None:
        if len(coords) == 2:
            self.board[coords[0], coords[1]] = (self.board[coords[0], coords[1]] + 1) % 2  #flip the dot
        else:
            print("Invalid coordinate dimension")
            
    def get_board(self) -> np.ndarray:
        return self.board
    
    def __repr__(self) -> str:
        print(type(self.board))
        output_String = np.array2string(self.board, formatter={'float':lambda x: self.on if x else self.off})

        return re.sub(' ','', re.sub('[\[\]]', '', output_String))
    
    
    def save_board(self) -> None:
        pickle.dump(self.board, open(self.filename, "wb"))
        
    def load_board(self) -> None:
        if os.path.isfile(self.filename):
            board_loading=pickle.load(open(self.filename, "rb"))
            
            if self.board.shape != board_loading.shape:
                pass
            else:
                self.board=board_loading
                
        

if __name__ == '__main__':
    pass