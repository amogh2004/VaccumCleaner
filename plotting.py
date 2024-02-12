import numpy as np
import matplotlib.pyplot as plt
from environment import Environment

class VisualizeAgents:
    def __init__(self, env, agent, steps=100):
        self.env = env
        self.agent = agent
        self.steps = steps

    def visualize_floor_before(self):
        plt.title(str(self.agent) + ' Floor Before')
        plt.imshow(self.env.floor, cmap='Blues', interpolation='nearest')
        plt.show()

    def visualize_agentPath_before(self):
        plt.title(str(self.agent) + ' Path Before')
        plt.imshow(self.env.agent_has_been, cmap='Blues', interpolation='nearest')
        plt.show()
    
    def visualize_floor_after(self):
        plt.title(str(self.agent) + ' Floor After')
        plt.imshow(self.env.floor, cmap='Blues', interpolation='nearest')
        plt.show()
    
    def visualize_agentPath_after(self):
        plt.title(str(self.agent) + ' Path After')
        plt.imshow(self.env.agent_has_been, cmap='Blues', interpolation='nearest')
        plt.show()
