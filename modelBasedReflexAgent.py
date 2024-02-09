import numpy as np
import random
from environment import Environment


class ModelBasedReflexAgent:

    def __init__(self, start_x, start_y):
        self.curr_x = start_x
        self.curr_y = start_y
        self.history = {}

    def action(self, env):
        act = self.__model_based_reflex_action(env)
        self.__update_environment(env)
        self.__update_agent_path(act)

    def __model_based_reflex_action(self, env):
        if self.history.get((self.curr_x, self.curr_y)) == "Dirty":
            return "SUCK"
        else:
            return self.__random_movement()

    def __update_environment(self, env):
        env.update_env(self.curr_x, self.curr_y)

    def __update_agent_path(self, action):
        if action == "UP":
            self.curr_x = max(self.curr_x - 1, 0)
        elif action == "DOWN":
            self.curr_x = min(self.curr_x + 1, env.height - 1)
        elif action == "LEFT":
            self.curr_y = max(self.curr_y - 1, 0)
        elif action == "RIGHT":
            self.curr_y = min(self.curr_y + 1, env.width - 1)

    def __random_movement(self):
        return random.choice(["UP", "DOWN", "LEFT", "RIGHT"])

    def visualize_agent_movement(self, env):
        print("Agent current position:", self.curr_x, self.curr_y)


# Test the implementation
M = 10
N = 10
dirt_percentage = 20

env = Environment(M, N)
env.add_dirt(dirt_percentage)

start_x = M // 2
start_y = N // 2

agent = ModelBasedReflexAgent(start_x, start_y)

# Running the agent for a few steps
for _ in range(100):
    agent.action(env)

env.visualize()
print(env.get_stats())
