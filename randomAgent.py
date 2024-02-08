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