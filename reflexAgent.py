import random
from environment import Environment

class reflexAgent:
    def __init__(self, start_x, start_y):
        self.curr_x = start_x
        self.curr_y = start_y
        self.path = [(start_x, start_y)]
        self.dirty_cells_cleaned = [0]
    def update_environment(self, env):
        env.update_env(self.curr_x, self.curr_y)

    def update_agent_path(self, action):
        if action == "UP":
            self.curr_x -= 1
        elif action == "DOWN":
            self.curr_x += 1
        elif action == "LEFT":
            self.curr_y -= 1
        elif action == "RIGHT":
            self.curr_y += 1

    def action(self, env):
        act = self.__reflex_action(env)
        #update the env
        if act == "SUCK":
            self.update_environment(env)
            self.dirty_cells_cleaned.append(self.dirty_cells_cleaned[-1] + 1)
        else:
        #update agent path
            self.update_agent_path(act)
            self.path.append((self.curr_x, self.curr_y))
        
    def __reflex_action(self, env):
        #add functionality to return a reflex action
        R = env.get_bounds()[1]
        C = env.get_bounds()[0]
        env.update_agent_path(self.curr_x, self.curr_y)

        if env.is_dirty(self.curr_x, self.curr_y):
            return "SUCK"
        elif self.curr_x == 0 and self.curr_y == 0:
            return random.choice(["DOWN", "RIGHT"]) 
        elif self.curr_x == 0 and self.curr_y == C - 1:
            return random.choice(["DOWN", "LEFT"])
        elif self.curr_x == R - 1 and self.curr_y == 0:
            return random.choice(["RIGHT", "UP"])
        elif self.curr_x == R - 1 and self.curr_y == C - 1:
            return random.choice(["LEFT", "UP"])
        elif self.curr_x == 0: 
            return random.choice(["DOWN", "RIGHT", "LEFT"])
        elif self.curr_x == R - 1: 
            return random.choice(["RIGHT", "LEFT", "UP"])  
        elif self.curr_y == 0: 
            return random.choice(["DOWN", "RIGHT", "UP"])
        elif self.curr_y == C - 1: 
            return random.choice(["DOWN", "LEFT", "UP"])  
        else:
            return random.choice(["DOWN", "UP", "LEFT", "RIGHT"])
       
    def visualize_agent_movement(self, env):
        #add functionality to visualize environment 
        print(self.curr_x, self.curr_y)
    
    def __str__(self):
        return 'Reflex Agent'




