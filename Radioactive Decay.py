import math  # importing math library to use log function
import random  # importing random library to generate random number between 0 and 1
import numpy as np


class NucleiArray:  # defining class to create array of nuclei object
    # defining the __init__ method to assign the properties of the array of nuclei
    def __init__(self, length, decay_constant, time_step):
        # probability of decay at given time step
        self.probability = decay_constant * time_step
        self.length = length  # number of undecayed nuclei
        self.decayed = 0  # number of decayed nuclei
        # creating nested list to represent array of nuclei
        self.array = np.ones((length, length))

    def decay(self):  # method to run the decay process
        counter = 0  # initialising counter variable
        while self.decayed < self.length ** 2 / 2:
            counter += 1
            for x in range(self.length):
                for y in range(self.length):
                    # comparing a random number to probability
                    if self.array[x, y] == 1 and random.random() < self.probability:
                        self.array[x, y] = 0  # marking nucleus as decayed
                        self.decayed += 1  # changing count of decayed nuclei
        return counter

    def visual(self):  # method to produce visual representation of array of nuclei
        for x in range(len(self.array)):
            for y in range(len(self.array)):
                print(int(self.array[x, y]), end=" ")
            print()


def main():  # main method to creat array object and call relevant functions
    # accepting decay constant from user
    decay_constant = float(input("Enter decay constant: "))
    # accepting length of array from user
    length_of_array = int(input("Enter length of array: "))
    time_step = float(input("Enter timestep in minutes: ")
                      )  # accepting time step from user
    # creating array of nuclei object
    n_1 = NucleiArray(length_of_array, decay_constant, time_step)
    time_elapsed = time_step * n_1.decay()  # initialising elapsed time variable

    print("Visual: ")
    n_1.visual()  # calling the relevant method for visual representation of array
    print("Initial Undecayed: " + str(n_1.length ** 2))
    print("Final Undecayed: " + str(n_1.length ** 2 - n_1.decayed))
    print("Simulated Half-Life: " + str(time_elapsed) + " min")
    print("Predicted Half-Life: " + str(math.log(2)/decay_constant) + " min")


main()  # calling main
