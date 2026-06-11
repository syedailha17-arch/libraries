import numpy as np
"""Rules:

Burning trees become empty.
Trees next to a burning tree catch fire.
Empty cells stay empty.

Given an initial forest, compute the next generation.

Goal: Use NumPy slicing and masks instead of nested loops.
0 = empty
1 = tree
2 = burning"""


def next_generation(forest):
    trees = forest == 1
    burning = forest == 2

    near_fire = np.zeros_like(burning, dtype=bool)

    # Up
    near_fire[:-1, :] |= burning[1:, :]

    # Down
    near_fire[1:, :] |= burning[:-1, :]

    # Left
    near_fire[:, :-1] |= burning[:, 1:]

    # Right
    near_fire[:, 1:] |= burning[:, :-1]

    # Diagonals
    near_fire[:-1, :-1] |= burning[1:, 1:]     # Down-right
    near_fire[:-1, 1:] |= burning[1:, :-1]     # Down-left
    near_fire[1:, :-1] |= burning[:-1, 1:]     # Up-right
    near_fire[1:, 1:] |= burning[:-1, :-1]     # Up-left

    next_forest = forest.copy()

    # Burning trees become empty
    next_forest[burning] = 0

    # Trees adjacent to fire catch fire
    next_forest[trees & near_fire] = 2

    return next_forest

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(cols):
        value = int(input(f"Enter element at ({i}, {j}): "))
        row.append(value)
    matrix.append(row)

forest = np.array(matrix)

print("Old forest:")
print(forest)

print("Next generation:")
print(next_generation(forest))