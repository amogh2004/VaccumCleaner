from environment import Environment
import numpy as np


class ModelBasedReflexAgent:
    def __init__(self, environment):
        self.environment = environment
        self.location = (0, 0)  # Starting at the top-left corner
        self.model = {
            "PerceptHistory": {}  # Initializing percept history
        }

    def sense(self):
        # Sensing the current location's state and update the agent's model
        x, y = self.location
        percept = "Dirty" if self.environment.is_dirty(x, y) else "Clean"
        self.model["PerceptHistory"][self.location] = percept

    def act(self):
        # Deciding the action based on the percept history
        C, R= self.environment.get_bounds()
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
            if x > 0: possible_moves.append("Up")
            if x < R-1: possible_moves.append("Down")
            if y > 0: possible_moves.append("Left")
            if y < C-1: possible_moves.append("Right")
            return np.random.choice(possible_moves)

    def move(self, action):
        # Moving the agent according to the action
        C, R= self.environment.get_bounds()
        x, y = self.location
        if action == "Suck":
            self.environment.update_env(x, y)
        elif action == "Down" and x < R-1:
            self.location = (x+1, y)
        elif action == "Up" and x>0:
            self.location = (x-1, y)
        elif action == "Right" and y<C-1:
            self.location = (x, y+1)
        elif action == "Left" and y>0:
            self.location = (x, y-1)

# test
M = 10
N = 10
dirt_percentage = 20

env = Environment(M, N)
env.add_dirt(dirt_percentage)

agent = ModelBasedReflexAgent(env)

# Running the agent for a few steps
for _ in range(100):
    agent.sense()
    action = agent.act()
    agent.move(action)

env.visualize()
print(env.get_stats())
