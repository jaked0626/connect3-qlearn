import numpy as np

class Board(object):

    def __init__(self, player1='x', player2='o', verbose=True):
        """
        Initialize board
        Inputs: 
          player (str): piece of player_one this board revolves around
        """
        self.reset()
        self.player1 = player1
        self.player2 = player2
        self.verbose = verbose
    
    def reset(self):
        self.board = np.zeros(shape=(3,3), dtype=str)
        self.col_map = {
            'L': 0,
            'C': 1,
            'R': 2,
            'l': 0,
            'c': 1,
            'r': 2,
            '0': 0,
            '1': 1,
            '2': 2,
            0  : 0,
            1  : 1,
            2  : 2,  
        }
        self.last_play = (0, 3)
        self.game_over = False
        self.win = False
        self.lose = False
        self.moves = 0
    
    def insert(self, col):
        """
        Inserts player's sign into specified column
        Inputs:
            col (str): one of "L", "C", "R", indicating left, 
                center, right columns respectively
            piece (str): player's piece ("O", "X", etc)
        """
        piece = self.player2 if self.moves else self.player1
        self.moves = (self.moves + 1) % 2
        col = self.col_map.get(col)
        for i in range(2, -1, -1):
            #print(i, col)
            #print(self.board[i, col])
            if self.board[i, col]: continue
            self.board[i, col] = piece
            self.last_play = (i, col)
            self.__check_victory()
            break
        else:
            print('move is invalid')
        
        self.__check_full()
    
    def __check_victory(self):
        """
        checks board after every move to see if game is over.
        """
        row, col = self.last_play
        # check for vertical, horizontal, and diagonal matches
        if (self.board[row, col] == self.board[(row+1)%3, col] == self.board[(row+2)%3, col]) or \
           (self.board[(row, col)] == self.board[row, (col+1)%3] == self.board[row, (col+2)%3]) or \
           (row == col and 
           (self.board[row, col] == self.board[(row+1)%3, (col+1)%3] == self.board[(row+2)%3, (col+2)%3])) or\
           ((row + col == 2) and
           (self.board[row, col] == self.board[(row-1)%3, (col+1)%3] == self.board[(row-2)%3, (col+2)%3])):
            self.game_over = True
            self.win = self.board[row, col] == self.player1
            self.lose = not self.win
            if self.verbose: self.__announce_gameover()
    
    def __announce_gameover(self):
        if self.win:
            print(f'player one ("{self.player1}") wins!')
        elif self.lose:
            print(f'player two ("{self.player2}") wins!')
        else:
            print('draw!!')
        print(self)
    
    def flip(self):
        return np.flip(self.board, 1)
    
    def _flip_str(self):
        return self.__str__(flip=True)
    
    def __check_full(self):
        full = np.all((self.board[0,]=='') == False)
        if full:
            self.game_over = True
            if self.verbose: self.__announce_gameover()
        return full
    
    def hash(self, flip=False):
        board = self.flip() if flip else self.board
        num = ''
        for row in range(3):
            for col in range(3):
                if board[row, col] == self.player1:
                    num += '1'
                elif board[row, col] == self.player2:
                    num += '2'
                else:
                    num += "0"
        
        return int(num, base=3)
    
    def hash_to_board(self, num):
        ternary = np.base_repr(num,base=3)
        while len(ternary) < 9:
            ternary = '0' + ternary
        counter = 0
        for row in range(3):
            for col in range(3):
                if ternary[counter] == '1':
                    self.board[row, col] = self.player1
                elif ternary[counter] == '2':
                    self.board[row, col] = self.player2
                else:
                    self.board[row, col] = ''
                counter += 1

    def __str__(self, flip=False):
        board = self.flip() if flip else self.board
        s = ""
        for row in range(3):
            for col in range(3):
                if board[row, col]:
                    s += board[row, col]
                else:
                    s += '_'
            s += '\n'
        return s

    def __repr__(self):
        return self.__str__()




        
        




        