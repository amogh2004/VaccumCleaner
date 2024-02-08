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