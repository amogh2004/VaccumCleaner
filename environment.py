import numpy as np

class Environment:
    def __init__(self, width, height):
        # Initialize the environment with the specified width and height.
        # Sets up the floor grid and agent's path grid.
        self.width = width
        self.height = height
        self.floor = np.zeros((height, width))  # Initialize floor grid
        self.agent_has_been = np.zeros((height, width))  # Initialize agent's path grid

    def add_dirt(self, dirt_percentage):
        # Add dirt to the environment randomly based on the given percentage.
        total_cells = self.width * self.height
        num_dirt_cells = int((dirt_percentage / 100) * total_cells)
        dirt_positions = np.random.choice(total_cells, num_dirt_cells, replace=False)

        for pos in dirt_positions:
            row = pos // self.width
            col = pos % self.width
            self.floor[row][col] = 1

    def is_dirty(self, x, y):
        # Check if the specified tile (x, y) is dirty.
        return self.floor[y][x] == 1

    def get_bounds(self):
        # Get the bounds of the environment (width, height).
        return (self.width, self.height)

    def update_env(self, x, y):
        # Update the environment by removing dirt at the specified tile (x, y).
        if self.is_dirty(x, y):
            self.floor[y][x] = 0

    def update_agent_path(self, x, y):
        # Record the agent's path by marking the specified tile (x, y) as visited.
        self.agent_has_been[y][x] = 2

    def get_stats(self):
        # Get statistics about the environment, including total dirt and total clean tiles.
        total_dirt = np.sum(self.floor)
        total_clean = self.width * self.height - total_dirt
        return {"Total Dirt": total_dirt, "Total Clean": total_clean}

    def visualize(self):
        # Visualize the environment (floor) and the agent's path.
        print("Floor:")
        print(self.floor)
        print("Agent Path:")
        print(self.agent_has_been)


# Example usage:
M = 5
N = 5
dirt_percentage = 20

env = Environment(M, N)
env.add_dirt(dirt_percentage)
env.visualize()
print(env.get_stats())