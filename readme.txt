
README
Window Cleaning Simulator
This Python script simulates the time it takes to clean windows based on the number of windows in a house and their level of dirtiness. It prompts the user for input regarding the number of windows and their dirtiness level on a scale of 1 to 4, then calculates the time required to clean the windows accordingly.

Script Overview
Classes:
    House:
    Represents a house with attributes for the number of windows and their dirtiness level.
    Provides a method to calculate the time required to clean the windows based on their dirtiness level.
    Contains a dictionary to map dirtiness levels to corresponding descriptive strings.
Functions:
    checking(message):
    Displays a message character by character with a slight delay, simulating a checking process.
    Main Function:
main():
    Runs an input loop to get the number of windows and their dirtiness level from the user.
    Creates a House object with the provided parameters.
    Simulates a checking process.
    Calculates and displays the time required to clean the windows.
    Prints a closing message and exits the program.