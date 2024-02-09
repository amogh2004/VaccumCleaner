import numpy as np
from environment import Environment
class RandomAgent:

    def __init__(self, startX, startY):
        self.positionCol = startX
        self.positionRow = startY

    def action(self, env):
        #update agent environment
        env.update_agent_path(self.positionCol, self.positionRow)

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

    def randomAction(self):
        randomAct = np.random.choice(["up", "down", "right", "left"])
        return randomAct
        

    def visualize_agent_mevement(self, env):
        pass


#test
env = Environment(10, 10)
env.add_dirt(60)
agent = RandomAgent(5, 5)
env.visualize()
print(env.get_stats())

for i in range(100):
    result = agent.action(env)
    if(result == -1):
        break

env.visualize()
print(env.get_stats())



