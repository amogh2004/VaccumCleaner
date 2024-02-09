import numpy as np
import matplotlib.pyplot as plt
from environment import Environment

class VisualizeAgents:
    def __init__(self, env, agents, steps=100):
        self.env = env
        self.agents = agents
        self.steps = steps

    def run_simulation(self):
        for agent in self.agents:
            for _ in range(self.steps):
                agent.sense()
                action = agent.act()
                agent.move(action)

    def plot_performance_metrics(self):
        plt.figure(figsize=(10, 6))
        for agent in self.agents:
            plt.plot(range(len(agent.dirty_cells_cleaned)), agent.dirty_cells_cleaned, label=agent.__class__.__name__)
        plt.xlabel('Time Step')
        plt.ylabel('Dirty Cells Cleaned')
        plt.title('Performance Comparison of Agents')
        plt.legend()
        plt.grid(True)
        plt.show()

    def visualize_paths(self):
        plt.figure(figsize=(8, 8))
        self.env.visualize()
        for agent in self.agents:
            path = np.array(agent.path)
            plt.plot(path[:, 0], path[:, 1], label=agent.__class__.__name__, marker='o')
        plt.legend()
        plt.title('Paths Taken by Agents')
        plt.show()
