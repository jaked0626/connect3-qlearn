from board import Board
from more_itertools import distinct_permutations
import pickle

PERMS = distinct_permutations('000111222') # each column can only be chosen 3 times
COMBOS = set()

def simulate_board():
    # permutation with overlapping items n! / q! r! s! 
    # 9! / 3! 3! 3! = 1680
    b = Board(verbose=False)
    for perm in PERMS:
        #print(b.board)
        b.reset()
        simulate_one_perm(b, list(perm))

def simulate_one_perm(b: Board, perm: list):
    for move in perm:
        #print(move)
        b.insert(move)
        if b.hash(flip=False) not in COMBOS and b.hash(flip=True) not in COMBOS:
            COMBOS.add(b.hash())
        if b.game_over: break

def write_boards_in_hashed_form():
    with open('../board_options/hashed_boards.txt', 'w') as f:
        for hashed_board in sorted(COMBOS):
            f.write(str(hashed_board) + '\n')

def write_hashed_in_board_form():
    open('../board_options/unhashed_boards.txt', 'w').close() # clear file content if file already exists
    b = Board()
    with open('../board_options/hashed_boards.txt') as f:
        hashes = f.readlines()
    for hash in hashes:
        b.hash_to_board(int(hash))
        with open('../board_options/unhashed_boards.txt', 'a') as f:
            f.write(b.__str__())
            f.write('\n')
    



def main():
    simulate_board()
    write_boards_in_hashed_form()
    write_hashed_in_board_form()


if __name__ == '__main__':
    main()