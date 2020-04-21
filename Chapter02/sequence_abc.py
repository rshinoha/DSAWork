# Copyright 2013, Michael H. Goldwasser
#
# Developed for use with the book:
#
#    Data Structures and Algorithms in Python
#    Michael T. Goodrich, Roberto Tamassia, and Michael H. Goldwasser
#    John Wiley & Sons, 2013
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Reinforcement exercises R-2.22 and R-2.23
# Ryoh Shinohara
# =======================================================================================
# **R-2.22** The `collections.Sequence` abstract base class does not provide support for
# comparing two sequences to each other. Modify our `Sequence` class from Code Fragment
# 2.14 to include a definition for the `__eq__` method, so that expression `seq1 == seq2`
# will return `True` precisely when the two sequences are element by element equivalent.


from abc import ABCMeta, abstractmethod           # need these definitions

class Sequence(metaclass=ABCMeta):
  """Our own version of collections.Sequence abstract base class."""

  @abstractmethod
  def __len__(self):
    """Return the length of the sequence."""

  @abstractmethod
  def __getitem__(self, j):
    """Return the element at index j of the sequence."""

  def __contains__(self, val):
    """Return True if val found in the sequence; False otherwise."""
    for j in range(len(self)):
      if self[j] == val:                          # found match
        return True
    return False

  def index(self, val):
    """Return leftmost index at which val is found (or raise ValueError)."""
    for j in range(len(self)):
      if self[j] == val:                          # leftmost match
        return j
    raise ValueError('value not in sequence')     # never found a match

  def count(self, val):
    """Return the number of elements equal to given value."""
    k = 0
    for j in range(len(self)):
      if self[j] == val:                          # found a match
        k += 1
    return k

  def __eq__(self, other):
    """Returns True if two sequences are identical"""
    for j in range(len(self)):
      if self[j] != other[j]:
        return False
    return True
  
  def __lt__(self, other):
    """Returns True if self < other"""
    for j in range(len(self)):
      if self[j] < other[j]:
        return True
    return False

class Range(Sequence):
  """A class that mimic's the built-in range class."""

  def __init__(self, start, stop=None, step=1):
    """Initialize a Range instance.

    Semantics is similar to built-in range class.
    """
    if step == 0:
      raise ValueError('step cannot be 0')
      
    if stop is None:                  # special case of range(n)
      start, stop = 0, start          # should be treated as if range(0,n)

    # calculate the effective length once
    self._length = max(0, (stop - start + step - 1) // step)

    # need knowledge of start and step (but not stop) to support __getitem__
    self._start = start
    self._step = step

  def __len__(self):
    """Return number of entries in the range."""
    return self._length

  def __getitem__(self, k):
    """Return entry at index k (using standard interpretation if negative)."""
    if k < 0:
      k += len(self)                  # attempt to convert negative index

    if not 0 <= k < self._length:
      raise IndexError('index out of range')

    return self._start + k * self._step

if __name__ == "__main__":
  r1 = Range(10)          # [0, 1, ..., 9]
  r2 = Range(0,10,1)      # Same as r2
  r3 = Range(0,10,2)
  print(r1[5])            # print 5
  print(10 in r1)         # print False
  print(r1.index(5))      # print 5
  print(r1.count(5))      # print 1
  print(r1 == r2)         # print True
  print(r1 == r3)         # print False
  print(r1 > r2)          # print False
  print(r3 > r2)          # print True