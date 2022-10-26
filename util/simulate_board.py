from board import Board
from more_itertools import distinct_permutations

PERMS = distinct_permutations('000111222') # each column can only be chosen 3 times
COMBOS = set()

def simulate_board():
    global PERMS
    # permutation with overlapping items n! / q! r! s! 
    # 9! / 3! 3! 3! = 1680
    b = Board()
    for perm in PERMS:
        #print(b.board)
        b.reset()
        simulate_one_perm(b, list(perm))

def simulate_one_perm(b: Board, perm: list):
    global COMBOS
    for i, loc in enumerate(perm):
        player = (i % 2) + 1
        b.insert(int(loc), player)
        if b.stringify() not in COMBOS:
            print(b.stringify)
            COMBOS.add(b.stringify())
        if b.check_game_over():
            break

def write_boards():
    global COMBOS
    with open('../qcols.txt', 'w') as f:
        for board in COMBOS:
            f.write(board + '\n')

def main():
    print(COMBOS)
    simulate_board()
    print(COMBOS)
    write_boards()


if __name__ == '__main__':
    main()