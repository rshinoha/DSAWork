# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Project exercise P-2.36
# Ryoh Shinohara
# =======================================================================================
# Write a Python program to simulate an ecosystem containing two types of creatures,
# bears and fish. The ecosystem consists of a river, which is modeled as a relatively
# large list. Each element of the list should be a Bear object, a Fish object, or None.
# In each time step, based on a random process, each animal either attempts to move into
# an adjacent list location or stay where it is. If two animals of the same type are
# about to collide in the same cell, then they stay where they are, but they create a new
# instance of that type of animal, which is placed in a random empty (i.e., previously
# None) location in the list. If a bear and a fish collide, however, then the fish dies
# (i.e., it disappears).
from random import random, randrange

class River():
    """An object of River class"""

    def __init__(self, size=500, ratio=(1,100), density=0.5):
        """
        Creates a River object
        * size = size of the list simulating a river (default size of 1000)
        * ratio = Bear to Fish ratio (default ratio of 1 Bear per 100 fish)
        * density = population density of river (default of 0.5)
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 1:
            raise ValueError('size must be greater than 0')
        if len(ratio) != 2:
            raise TypeError('ratio must be a list or a tuple of length 2')
        if ratio[0] < 0 or ratio[1] < 0:
            raise ValueError('ratio must be positive')
        if density < 0 or density > 1:
            raise ValueError('density must be between 0 and 1')
        self._size = size
        self._ratio = ratio
        self._density = density
        self._river = [None for i in range(size)]
        # For generating a random number when deciding to add a Bear or a Fish
        ratio_denom = ratio[0] + ratio[1]
        for i in range(size):
            if random() > density:
                if randrange(ratio_denom) < ratio[0]:
                    self._river[i] = Bear()
                else:
                    self._river[i] = Fish()
    
    def print_river(self):
        """Prints the current state of the river"""
        print(['-' if i is None else ('B' if isinstance(i, Bear) else 'F') for i in self._river])

    def population(self):
        """Prints the current population of the river"""
        bear = 0
        fish = 0
        for i in self._river:
            if isinstance(i, Bear):
                bear += 1
            elif isinstance(i, Fish):
                fish += 1
        print("Bear: {}\tFish: {}".format(bear, fish))

class Bear():
    """An object of Bear class to populate the River class"""
    def __init__(self):
        """Creates an object of the Bear class"""

class Fish():
    """An object of Fish class to populate the River class"""
    def __init__(self):
        """Creates an object of the Fish class"""

if __name__ == "__main__":
    river = River()
    river.print_river()
    river.population()