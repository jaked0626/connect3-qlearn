from dataclasses import dataclass, field
import numpy as np

@dataclass
class Board:
    board: list = field(default_factory=list)

    def __post_init__(self):
        self.board = [0] * 9

    def insert(self, loc: int, symbol: int) -> bool:
        for i in range(loc, loc + 7, 3):
            if not self.board[i]:
                self.board[i] = symbol
                return True
        else:
            print("illegal move")
            return False
    
    def check_win(self):
        # horizontal win conditions
        if self.board[0] == self.board[1] == self.board[2] != 0:
            print (f"player {self.board[0]} wins")
            return self.board[0]
        elif self.board[3] == self.board[4] == self.board[5] != 0:
            print (f"player {self.board[3]} wins")
            return self.board[3]
        elif self.board[6] == self.board[7] == self.board[8] != 0:
            print (f"player {self.board[6]} wins")
            return self.board[4]
        # vertical win conditions
        elif self.board[0] == self.board[3] == self.board[6] != 0:
            print(f"player {self.board[0]} wins")
            return self.board[0]
        elif self.board[1] == self.board[4] == self.board[7] != 0:
            print(f"player {self.board[0]} wins")
            return self.board[1]
        elif self.board[2] == self.board[5] == self.board[8] != 0:
            print(f"player {self.board[0]} wins")
            return self.board[2]
        # diagonal win conditions
        elif self.board[0] == self.board[4] == self.board[8] != 0:
            print(f"player {self.board[4]} wins")
            return self.board[4]
        elif self.board[2] == self.board[4] == self.board[6] != 0:
            print(f"player {self.board[4]} wins")
            return self.board[4]
        else:
            winner = 3 if self.is_full() else 0
            return winner
    
    def is_full(self) -> bool:
        return 0 not in self.board
    
    def check_game_over(self) -> bool:
        """
        Returns 0 if game is not over, 1 if first player wins, 2 if second player wins, 
        3 if it is a draw.
        """
        winner = self.check_win()
        return winner

    def reset(self):
        self.__post_init__()
    
    def __str__(self):
        s = "".join(map(str, self.board[6:])) + "\n" \
            + "".join(map(str, self.board[3:6])) + "\n" \
            + "".join(map(str, self.board[:3]))
        return s
    
    def __repr__(self):
        return self.__str__()
    
    def stringify(self):
        return "".join(map(str, self.board))
    

        
        

        