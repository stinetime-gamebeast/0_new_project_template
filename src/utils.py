# Use utils.py to define useful functions which will be used in main.py

import itertools

def all_column_combos(list):
    result = []
    for i in range(1, len(list) + 1):
        result.extend(itertools.combinations(list, i))
    return result