import numpy as np

class Environment:
    def __init__ (self ,width, height) :
        self.width = width
        self.height = height
        self.floor = np.zeros ((height,width))
        self.agent_has_been = np.zeros((height,width))

    def add_dirt (self, dirt_percentage) :
    ## add functionality to change pass

    def is_dirty(self, x, y) :
    ## add functionality to see if a tile is dirty

    def get_bounds (self) :
    ## add functionality to return the bounds of the env

    def update_env(self, x,y) :
    ## add functionality to remove dirt diven coordinates pass

    def update_agent_path(self, x, y) :
    ## add functionality to record agent's path pass

    def get_stats (self) :
    ## add functionality to get stats pass

    def visualize(self):
    ## add functionality to visualize enu and agent path