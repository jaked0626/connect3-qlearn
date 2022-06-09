from util.board import Board
import pandas as pd

def load_q_table(filepath):
    with open(filepath, 'r') as f:
        qtable = [hash.strip() for hash in f.readlines() if hash != '']
    df = pd.DataFrame()
    df['board'] = qtable

    return df




