import numpy as np
import random

M = 5
N = 5
dirt_percentage = 20

def initialize_environment(M, N, dirt_percentage):
    environment = [[0 for _ in range(N)] for _ in range(M)]
    total_cells = M * N
    num_dirt_cells = int((dirt_percentage / 100) * total_cells)

    dirt_positions = random.sample(range(total_cells), num_dirt_cells)
    for pos in dirt_positions:
        row = pos // N
        col = pos % N
        environment[row][col] = 1

    return environment

environment = initialize_environment(M, N, dirt_percentage)
for row in environment:
    print(row)