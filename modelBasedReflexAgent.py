from environment import Environment
import random

class ModelBasedReflexAgent:
    def __init__(self, start_x, start_y):
        self.location = (start_x, start_y)  
        self.model = {
            "PerceptHistory": {}  # Initializing percept history
        }
    def sense(self, env):
        # Sensing the current location's state and update the agent's model
        x, y = self.location
        percept = "Dirty" if env.is_dirty(x, y) else "Clean"
        self.model["PerceptHistory"][self.location] = percept
    def act(self, env):
        # Deciding the action based on the percept history
        C, R= env.get_bounds()
        x, y = self.location
        if self.model["PerceptHistory"].get(self.location) == "Dirty":
            return "Suck"
        elif (x, y + 1) in self.model["PerceptHistory"] and self.model["PerceptHistory"][(x, y + 1)] == "Dirty":
            return "Down"
        elif (x, y - 1) in self.model["PerceptHistory"] and self.model["PerceptHistory"][(x, y - 1)] == "Dirty":
            return "Up"
        elif (x + 1, y) in self.model["PerceptHistory"] and self.model["PerceptHistory"][(x + 1, y)] == "Dirty":
            return "Right"
        elif (x - 1, y) in self.model["PerceptHistory"] and self.model["PerceptHistory"][(x - 1, y)] == "Dirty":
            return "Left"
        else:
            # If no dirty percept nearby, moves randomly
            possible_moves = []
            if y > 0: possible_moves.append("Up")
            if y < R-1: possible_moves.append("Down")
            if x > 0: possible_moves.append("Left")
            if x < C-1: possible_moves.append("Right")
            return random.choice(possible_moves)
    def move(self, action, env):
        # Moving the agent according to the action
        C, R= env.get_bounds()
        x, y = self.location
        if action == "Suck":
            env.update_env(x, y)
        elif action == "Down" and y < R-1:
            self.location = (x, y+1)
            env.update_agent_path(x, y+1)
        elif action == "Up" and y>0:
            self.location = (x, y-1)
            env.update_agent_path(x, y-1)
        elif action == "Right" and x<C-1:
            self.location = (x+1, y)
            env.update_agent_path(x+1, y)
        elif action == "Left" and x>0:
            self.location = (x-1, y)
            env.update_agent_path(x-1, y)

#test
env = Environment(10, 10)
env.add_dirt(20)
agent = ModelBasedReflexAgent(5, 5)
env.visualize()
print(env.get_stats())

for i in range(100):
    agent.sense(env)
    action=agent.act(env)
    agent.move(action, env)

env.visualize()
print(env.get_stats())
