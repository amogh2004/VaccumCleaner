import numpy as np
import random
from queue import Queue
from collections import deque

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

""" environment = initialize_environment(M, N, dirt_percentage)
for row in environment:
    print(row) """

def randomized_agent():
    environment = initialize_environment(M, N, dirt_percentage)

    dirtCount = 0
    positionRow = random.randint(1, N-1)
    positionCol = random.randint(1, M-1)

    if(environment[positionRow][positionCol] == 1):
        environment[positionRow][positionCol] = 0
        dirtCount += 1

    run = 0
    while(run < 15):        #15 runs
        randomAction = random.randrange(4)  # 0 -> up; 1 -> down; 2 -> right; 3 -> left
        match randomAction:
            case 0: positionRow += 1
            case 1: positionRow -= 1
            case 2: positionCol += 1
            case 3: positionCol -= 1

        if((positionRow < 0) or (positionRow >= N)):
            return dirtCount
        
        if((positionCol < 0) or (positionCol >= N)):
            return dirtCount

        if(environment[positionRow][positionCol] == 1):
            environment[positionRow][positionCol] = 0
            dirtCount += 1
        
        run += 1
    
    return dirtCount

def performance_Random_Agent():
    result = 0
    for _ in range(100):
        result += randomized_agent()
    print("Random_Agent:\nAverage performance of 100 runs is: %f" %(result / 100))
performance_Random_Agent()



def randomized_agent_Ash():
    M = 5 
    N = 5
    dirt_percentage = 70
    environment = initialize_environment(M, N, dirt_percentage)

    R, C = len(environment), len(environment[0])

    for i in range(R): 
        for j in range(C): 
            choice = random.choice(["UP", "DOWN", "LEFT", "RIGHT", "SUCK"])
            if choice == "UP": 
                if i == 0: 
                    break
            elif choice == "DOWN": 
                if i == R - 1:
                    break
            elif choice == "LEFT": 
                if j == 0: 
                    break
            elif choice == "RIGHT":
                if j == C - 1:
                    break
            else:
                return choice 

def reflex_agent(percepts, environment):
    
    R, C = len(environment), len(environment[0])

    rowPercept = percepts[0]
    colPercept = percepts[1]
    
    if environment[rowPercept][colPercept] == 1:
        environment[rowPercept][colPercept] == 0
        return "SUCK"
    if rowPercept == 0 and colPercept == 0:
        choice = random.choice(["DOWN", "RIGHT"])
        if choice == "DOWN": 
            percepts = [rowPercept + 1, colPercept]
            reflex_agent(percepts)
        elif choice == "RIGHT":
            percepts = [rowPercept, colPercept + 1]
            reflex_agent(percepts)
    elif rowPercept == 0 and colPercept == C - 1: 
        choice = random.choice(["DOWN", "LEFT"])
        if choice == "DOWN": 
            percepts = [rowPercept + 1, colPercept]
            reflex_agent(percepts)
        elif choice == "LEFT":
            percepts = [rowPercept, colPercept - 1]
            reflex_agent(percepts)
    elif rowPercept == R - 1 and colPercept == 0: 
        choice = random.choice(["RIGHT", "UP"])
        if choice == "UP": 
            percepts = [rowPercept - 1, colPercept]
            reflex_agent(percepts)
        elif choice == "RIGHT":
            percepts = [rowPercept, colPercept + 1]
            reflex_agent(percepts)
    elif rowPercept == R - 1 and colPercept == C - 1: 
        choice = random.choice(["LEFT", "UP"])
        if choice == "UP": 
            percepts = [rowPercept - 1, colPercept]
            reflex_agent(percepts)
        elif choice == "LEFT":
            percepts = [rowPercept, colPercept - 1]
            reflex_agent(percepts)
    else: 
        choice = random.choice(["UP", "DOWN", "LEFT", "RIGHT"])
        if choice == "UP": 
            percepts = [rowPercept - 1, colPercept]
            reflex_agent(percepts)
        elif choice == "RIGHT":
            percepts = [rowPercept, colPercept + 1]
            reflex_agent(percepts)
        elif choice == "LEFT":
            percepts = [rowPercept, colPercept - 1]
            reflex_agent(percepts)
        if choice == "DOWN": 
            percepts = [rowPercept + 1, colPercept]
            reflex_agent(percepts)
        
print(randomized_agent_Ash())
print("Second function")
print(reflex_agent([0,0]))




M = 5 
N = 5
dirt_percentage = 70
environment = initialize_environment(M, N, dirt_percentage)
print("Reflex environment")

dirtCount = 0
positionRow = random.randint(1, N-1)
positionCol = random.randint(1, M-1)
percepts = [positionRow, positionCol]
reflex_agent(environment, percepts)