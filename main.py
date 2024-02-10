import argparse  # Importing the argparse module for command-line argument parsing
from randomAgent import RandomAgent  # Importing the RandomAgent class from the randomAgent.py file
from reflexAgent import reflexAgent  # Importing the reflexAgent class from the reflexAgent.py file
from modelBasedReflexAgent import ModelBasedReflexAgent  # Importing the ModelBasedReflexAgent class from the modelBasedReflexAgent.py file

def main():
    """
    The main function to run the simulation of vacuum cleaner agents.
    """
    # Call the functions or instantiate the classes from each Python file
    RandomAgent(5, 5)  # Creating an instance of the RandomAgent class
    reflexAgent(5, 5)  # Creating an instance of the reflexAgent class
    ModelBasedReflexAgent(5, 5)  # Creating an instance of the ModelBasedReflexAgent class

if __name__ == "__main__":
    # Create an ArgumentParser object for parsing command-line arguments
    parser = argparse.ArgumentParser(description="Run simulation of vacuum cleaner agents.")
    # Add command-line arguments for specifying the environment dimensions and dirt percentage
    parser.add_argument("--rows", type=int, default=10, help="Number of rows in the environment")
    parser.add_argument("--columns", type=int, default=10, help="Number of columns in the environment")
    parser.add_argument("--dirt_percentage", type=int, default=20, help="Percentage of dirty cells in the environment (0-100)")
    # Parse the command-line arguments
    args = parser.parse_args()
    # Call the main function to execute the simulation
    main()

