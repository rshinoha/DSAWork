# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Reinforcement exercises R-2.9 to R-2.15
# Ryoh Shinohara
# =======================================================================================
# **R-2.9** Implement the `__sub__` method for the `Vector` class of Section 2.3.3, so
# that the expression $u−v$ returns a new vector instance representing the difference
# between two vectors.
#
# **R-2.10** Implement the `__neg__` method for the `Vector` class of Section 2.3.3, so
# that the expression $−v$ returns a new vector instance whose coordinates are all the
# negated values of the respective coordinates of $v$.
#
# **R-2.11** In Section 2.3.3, we note that our `Vector` class supports a syntax such as
# $v = u + [5, 3, 10, −2, 1]$, in which the sum of a vector and list returns a new vector.
# However, the syntax $v = [5, 3, 10, −2, 1] + u$ is illegal. Explain how the `Vector`
# class definition can be revised so that this syntax generates a new vector.
#
# **R-2.12** Implement the `__mul__` method for the `Vector` class of Section 2.3.3, so
# that the expression $v*3$ returns a new vector with coordinates that are 3 times the
# respective coordinates of $v$.
#
# **R-2.13** Exercise R-2.12 asks for an implementation of `__mul__`, for the `Vector`
# class of Section 2.3.3, to provide support for the syntax $v*3$. Implement the
# `__rmul__` method, to provide additional support for syntax $3*v$.
#
# **R-2.14** Implement the `__mul__` method for the `Vector` class of Section 2.3.3, so
# that the expression $u*v$ returns a scalar that represents the dot product of the
# vectors, that is, $\sum_{i=1}^d u_i \cdot v_i$.
#
# **R-2.15** The `Vector` class of Section 2.3.3 provides a constructor that takes an
# integer $d$, and produces a d-dimensional vector with all coordinates equal to 0.
# Another convenient form for creating a new vector would beto send the constructor a
# parameter that is some iterable type representing a sequence of numbers, and to
# create a vector with dimension equal to the length of that sequence and coordinates
# equal to the sequence values. For example,`Vector([4, 7, 5])` would produce a
# three-dimensional vector with coordinates $<4, 7, 5>$. Modify the constructor so that
# either of these forms is acceptable; that is, if a single integer is sent, it
# produces a vector of that dimension with all zeros, but if a sequence of numbers is
# provided, it produces a vector with coordinates based on that sequence.

import collections

class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        if isinstance(d, int):
            self._coords = [0] * d
        # R-2.15 solution (provided by the author for some reason...)
        else:                                  
            try:                                     # we test if param is iterable
                self._coords = [val for val in d]
            except TypeError:
                raise TypeError('invalid parameter type')

    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return jth coordinate of vector."""
        return self._coords[j]

    def __setitem__(self, j, val):
        """Set jth coordinate of vector to given value."""
        self._coords[j] = val

    def __add__(self, other):
        """Return sum of two vectors."""
        if len(self) != len(other):          # relies on __len__ method
            raise ValueError('dimensions must agree')
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    # R-2.11 solution
    # Because Python looks at the documentation of the left operand to check how to
    # process the right operand using the operator of interest, the right operand object
    # must be a part of objects that can be processed with the left operand. In this
    # case, `Vector` objects aren't included in possible objects that can be processed by
    # a `list` object. Therefore, we must create a `__radd__` method, which checks the
    # right operand class definition for ways to process an operator

    # Implementation of R-2.11
    def __radd__(self, other):
        """Returns sum of two vectors when left operand is not a Vector type"""
        return self + other

    # R-2.9 solution
    def __sub__(self, other):
        """Return difference of two vectors."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    # Implementation of R-2.11
    def __rsub__(self, other):
        """Returns difference of two vectors when right operand is not a Vector type"""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = other[j] - self[j]
        return result

    def __mul__(self, other):
        """
        Returns a scalar multiple if other is a number or a dot product if another Vector or list
        """
        # R-2.12 solution
        if isinstance(other, (int, float, complex)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = other * self[j]
            return result
        # R-2.14 solution
        else:
            result = 0
            for i in range(len(self)):
                for j in range(len(other)):
                    result += self[i] * other[j]
            return result

    def __rmul__(self, other):
        """
        Returns a scalar multiple if right operand is a number or a dot product if another Vector or list
        """
        # R-2.13 solution
        if isinstance(other, (int, float, complex)):
            result = Vector(len(self))
            for j in range(len(self)):
                result[j] = other * self[j]
            return result
        # R-2.14 solution
        else:
            result = 0
            for i in range(len(self)):
                for j in range(len(other)):
                    result += self[i] * other[j]
            return result

    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords

    def __ne__(self, other):
        """Return True if vector differs from other."""
        return not self == other             # rely on existing __eq__ definition

    def __str__(self):
        """Produce string representation of vector."""
        return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation

    # R-2.10 solution (was in source code provided by authors for some reason...)
    def __neg__(self):
        """Return copy of vector with all coordinates negated."""
        result = Vector(len(self))           # start with vector of zeros
        for j in range(len(self)):
            result[j] = -self[j]
        return result

    def __lt__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords < other._coords

    def __le__(self, other):
        """Compare vectors based on lexicographical order."""
        if len(self) != len(other):
            raise ValueError('dimensions must agree')
        return self._coords <= other._coords

if __name__ == '__main__':
    # the following demonstrates usage of a few methods
    v = Vector(5)              # construct five-dimensional <0, 0, 0, 0, 0>
    v[1] = 23                  # <0, 23, 0, 0, 0> (based on use of __setitem__)
    v[-1] = 45                 # <0, 23, 0, 0, 45> (also via __setitem__)
    print(v[4])                # print 45 (via __getitem__)
    u = v + v                  # <0, 46, 0, 0, 90> (via __add__)
    print(u)                   # print <0, 46, 0, 0, 90>
    u = v - v                  # <0, 0, 0, 0, 0> (via __sub__)
    print(u)                   # print <0, 0, 0, 0, 0>
    w = [2, 2, 2, 2, 2]        # a list to be used as a vector
    u = w + v                  # <2, 25, 2, 2, 47>
    print(u)                   # print <2, 25, 2, 2, 47>
    u = v + w                  # <2, 25, 2, 2, 47>
    print(u)                   # print <2, 25, 2, 2, 47>
    u = w - v                  # <2, -21, 2, 2, -43>
    print(u)                   # print <2, -21, 2, 2, -43>
    u = v - w                  # <-2, 21, -2, -2, 43>
    print(u)                   # print <-2, 21, -2, -2, 43>
    s = 3
    u = v * 3                  # <0, 69, 0, 0, 135>
    print(u)                   # print <0, 69, 0, 0, 135>
    u = v * v
    print(u)                   # print 4624
    u = 3 * v                  # <0, 69, 0, 0, 135>
    print(u)                   # print <0, 69, 0, 0, 135>
    s = [2, 0]
    u = v * s 
    print(u)                   # print 136
    v2 = Vector([1,2,3,4,5])
    print(v2)

    total = 0                  
    for entry in v:            # implicit iteration via __len__ and __getitem__
        total += entry