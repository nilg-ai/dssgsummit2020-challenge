"""
Script that computes the cost function of a given keyboard layout and text
corpus
"""

import argparse
import heapq
import numpy as np


from utils import check_keyboard, compute_cell_location


def get_args():
    """
    Parse the arguments from the terminal
    """

    descr = 'Compute the performance of a given keyboard.'
    parser = argparse.ArgumentParser(description=descr)
    parser.add_argument('--corpus', metavar='C', type=str,
                        default='data/en-corpus.txt',
                        help='Validation corpus')
    parser.add_argument('--valid-keys', metavar='V', type=str,
                        default='data/en-keys.txt',
                        help='Filename with the valid keys')
    parser.add_argument('--keyboard', metavar='K', type=str,
                        required=True,
                        help='Keyboard assignment')

    return parser.parse_args()


def compute_cost(keyboard, corpus):
    """Computes the cost of using a keyboard for a certain corpus"""

    mapping = {k: [] for k in set(keyboard)
               if k != ''}

    for i, char in enumerate(keyboard):
        if char != '':
            mapping[char].append(i)

    pending = [(0, -1, 0)]
    min_cost = np.ones(len(corpus)) * np.inf

    while pending:
        node = heapq.heappop(pending)
        node_cost, node_char_idx, node_key_idx = node

        if node_char_idx + 1 == len(corpus):
            return node_cost

        if min_cost[node_char_idx] < node_cost:
            continue
        min_cost[node_char_idx] = node_cost

        if not mapping.get(corpus[node_char_idx + 1]):
            print("Missing char: '%s'" % corpus[node_char_idx + 1])
            break

        for next_pos in mapping.get(corpus[node_char_idx + 1], []):
            next_cost = node_cost + \
                np.sqrt(np.sum(np.square(COORDS[next_pos] -
                                         COORDS[node_key_idx])))

            heapq.heappush(pending,
                           (next_cost, node_char_idx + 1, next_pos))

    return np.inf


ARGS = get_args()

with open(ARGS.valid_keys, 'r') as f:
    VALID_CHARS = f.read()[:-1]

# Get the corpus
with open(ARGS.corpus, 'r') as f:
    CORPUS = f.read().strip()

# Initialize the variables
COORDS = compute_cell_location()

# Read the assigment
ASSIGNMENT = ARGS.keyboard
ASSIGNMENT = [k if k != '_' else "" for k in ASSIGNMENT]

# Validate the keyboard
check_keyboard(ASSIGNMENT, VALID_CHARS)

# Compute cost
print('Cost:', compute_cost(ASSIGNMENT, CORPUS))
