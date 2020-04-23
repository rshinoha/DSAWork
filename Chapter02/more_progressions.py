# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Creativity exercise C-2.31 and C2.32
# Ryoh Shinohara
# =======================================================================================
# **C-2.31** Write a Python class that extends the `Progression` class so that each value
# in the progression is the absolute value of the difference between the previous two
# values. You should include a constructor that accepts a pair of numbers as the first
# two values, using 2 and 200 as the defaults.
#
# **C-2.32** Write a Python class that extends the `Progression` class so that each value
# in the progression is the square root of the previous value. (Note that you can no
# longer represent each value with an integer.) Your constructor should accept an optional
# parameter specifying the start value, using 65,536 as a default.

from progressions import Progression

class AbsoluteDifference(Progression):
    """Creates a sequence separated by the difference of the first two values"""
    def __init__(self, first=2, second=200):
        """
        Creates new absolute difference sequence
        
        first = first term of progression
        second = second term of progression
        step = step size
        """
        super().__init__(first)
        self._second = second
        self._step = abs(second - first)

    def _advance(self):
        """Advances sequence by _step in the positive direction"""
        self._current, self._second = self._second, self._second + self._step

class SqrtProgession(Progression):
    """Creates a sequence that takes a sqaure root at each step"""
    def __init__(self, first=65536):
        """
        Creates a new square root sequence

        first = first term of sequence
        """
        if first < 0:
            raise ValueError('value must be positive')
        super().__init__(first)

    def _advance(self):
        """Advances sequence by taking a sqaure root of the current value"""
        self._current = pow(self._current, 1/2)

if __name__ == "__main__":
    print("Default absolute difference starting with 2 and 200")
    AbsoluteDifference().print_progression(10)

    print("Absolute difference starting with -20 and 0")
    AbsoluteDifference(-20,0).print_progression(10)

    print("Absolute difference starting with 20 and 0 (starts increasing after second number)")
    AbsoluteDifference(20,0).print_progression(10)

    print("Default square root progression starting with 65,536")
    SqrtProgession().print_progression(10)

    print("Square root progression starting with 43,046,721")
    SqrtProgession(43046721).print_progression(10)