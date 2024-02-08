import numpy as np

class RandomizedAgent:
    def __init__(self, environment):
        # Initialize the randomized agent with the environment.
        self.environment = environment

    def random_move(self):
        # Move randomly in the environment (up, down, left, right) and perform a 'suck' action with a certain probability.
        # Get current position of the agent
        width, height = self.environment.get_bounds()
        x, y = np.random.randint(0, width), np.random.randint(0, height)

        # Perform a random action (move or suck)
        action = np.random.choice(['up', 'down', 'left', 'right', 'suck'])

        if action == 'up':
            y = max(0, y - 1)
        elif action == 'down':
            y = min(height - 1, y + 1)
        elif action == 'left':
            x = max(0, x - 1)
        elif action == 'right':
            x = min(width - 1, x + 1)
        elif action == 'suck':
            self.environment.update_env(x, y)  # Clean the current tile

        # Record the agent's path
        self.environment.update_agent_path(x, y)

        return x, y


# Example usage:
M = 5
N = 5
dirt_percentage = 20

env = Environment(M, N)
env.add_dirt(dirt_percentage)

agent = RandomizedAgent(env)

# Perform random moves for a certain number of steps
num_steps = 10
for _ in range(num_steps):
    x, y = agent.random_move()
    print(f"Agent moved to position: ({x}, {y})")
    print(env.get_stats())
    print("--------------------")