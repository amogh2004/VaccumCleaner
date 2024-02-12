import numpy as np
from environment import Environment
import matplotlib.pyplot as plt 
class RandomAgent:

    def __init__(self, startX, startY):
        self.positionCol = startX
        self.positionRow = startY
        self.path = [(startX, startY)]
        self.dirty_cells_cleaned = [0]
        


    def action(self, env):
        #update agent environment
        env.update_agent_path(self.positionCol, self.positionRow)
        self.path.append((self.positionCol, self.positionCol))

        act = self.randomAction()
        match act:
            case "up"   : self.positionRow -= 1
            case "down" : self.positionRow += 1
            case "right": self.positionCol += 1
            case "left" : self.positionCol -= 1

        # stop vacuum if outside the grid
        if((self.positionRow < 0) or (self.positionRow >= env.get_bounds()[1])):
            return -1
        
        if((self.positionCol < 0) or (self.positionCol >= env.get_bounds()[0])):
            return -1

        #check if dirty and update the floor environment
        if(env.is_dirty(self.positionCol, self.positionRow)):
            env.update_env(self.positionCol, self.positionRow)
            self.dirty_cells_cleaned.append(self.dirty_cells_cleaned[-1] + 1)

    def randomAction(self):
        randomAct = np.random.choice(["up", "down", "right", "left"])
        return randomAct


    def __str__(self):
        return 'Random Agent'






