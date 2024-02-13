import argparse  # Importing the argparse module for command-line argument parsing
from randomAgent import RandomAgent  # Importing the RandomAgent class from the randomAgent.py file
from reflexAgent import reflexAgent  # Importing the reflexAgent class from the reflexAgent.py file
from modelBasedReflexAgent import ModelBasedReflexAgent  # Importing the ModelBasedReflexAgent class from the modelBasedReflexAgent.py file
from environment import Environment
from plotting import VisualizeAgents

def main(rows, columns, dirt_percentage):
    """
    The main function to run the simulation of vacuum cleaner agents.
    """
    # Call the functions or instantiate the classes from each Python file



#---------------Random Agent average of 100 runs-----------#
    afterRandomAgent = []
    for ii in range(100):
        env=Environment(rows, columns)
        env.add_dirt(dirt_percentage)
        agent=RandomAgent(2, 2) # Creating an instance of the RandomAgent class

        dirty_tiles = env.get_stats()

        for i in range(100):
            res=agent.action(env)
            if (res==-1):
                break

        afterRandomAgent.append(dirty_tiles - env.get_stats())

    print('Average number of Tiles cleaned from Random Agent is: ' + str(sum(afterRandomAgent)/len(afterRandomAgent)))

    #plotting one run
    env1 = Environment(rows, columns)
    env1.add_dirt(dirt_percentage)
    agent1=RandomAgent(2, 2)
    visualizer1 = VisualizeAgents(env1, agent1)

    visualizer1.visualize_floor_before()
    visualizer1.visualize_agentPath_before()

    for i in range(100):
        res=agent1.action(env1)
        if (res==-1):
            break

    visualizer1.visualize_floor_after()
    visualizer1.visualize_agentPath_after()


#----------------Reflex Agent average of 100 runs--------------#

    afterReflexAgent = []
    for ii in range(100):
        env = Environment(rows, columns)
        env.add_dirt(dirt_percentage)

        agent=reflexAgent(2, 2) # Creating an instance of the RandomAgent class

        dirty_tiles = env.get_stats()

        for i in range(100):
            res=agent.action(env)

        afterReflexAgent.append(dirty_tiles - env.get_stats())

    print('Average number of Tiles cleaned from Reflex Agent is: ' + str(sum(afterReflexAgent)/len(afterReflexAgent)))

    #plotting one run
    env2 = Environment(rows, columns)
    env2.add_dirt(dirt_percentage)
    agent2=reflexAgent(2, 2)
    visualizer2 = VisualizeAgents(env2, agent2)

    visualizer2.visualize_floor_before()
    visualizer2.visualize_agentPath_before()

    for i in range(100):
        res=agent2.action(env2)

    visualizer2.visualize_floor_after()
    visualizer2.visualize_agentPath_after()


#-------------Model Based Reflex Agent average of 100 runs-----------#

    afterModelReflexAgent = []
    for ii in range(100):
        env = Environment(rows, columns)
        env.add_dirt(dirt_percentage)

        agent=ModelBasedReflexAgent(2, 2) # Creating an instance of the RandomAgent class

        dirty_tiles = env.get_stats()

        for i in range(100):
            agent.sense(env)
            action=agent.act(env)
            agent.move(action, env)

        afterModelReflexAgent.append(dirty_tiles - env.get_stats())

    print('Average number of Tiles cleaned from Model Reflex Agent is: ' + str(sum(afterModelReflexAgent)/len(afterModelReflexAgent)))

    #plotting one run
    env3 = Environment(rows, columns)
    env3.add_dirt(dirt_percentage)
    agent3=ModelBasedReflexAgent(2, 2)
    visualizer3 = VisualizeAgents(env3, agent3)

    visualizer3.visualize_floor_before()
    visualizer3.visualize_agentPath_before()

    for i in range(100):
        agent3.sense(env3)
        action=agent3.act(env3)
        agent3.move(action, env3)

    visualizer3.visualize_floor_after()
    visualizer3.visualize_agentPath_after()





if __name__ == "__main__":
    # Create an ArgumentParser object for parsing command-line arguments
    parser = argparse.ArgumentParser(description="Run simulation of vacuum cleaner agents.")
    # Add command-line arguments for specifying the environment dimensions and dirt percentage
    parser.add_argument("--rows", type=int, default=10, help="Number of rows in the environment")
    parser.add_argument("--columns", type=int, default=10, help="Number of columns in the environment")
    parser.add_argument("--dirt_percentage", type=int, default=20, help="Percentage of dirty cells in the environment (0-100)")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Accessing the rows, columns, and dirt_percentage variables
    rows = args.rows
    columns = args.columns
    dirt_percentage = args.dirt_percentage

    # Call the main function to execute the simulation
    main(rows, columns, dirt_percentage)

