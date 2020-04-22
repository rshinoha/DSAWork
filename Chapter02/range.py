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
# Creativity exercise C-2.27
# Ryoh Shinohara
# =======================================================================================
# **C-2.27** In Section 2.3.5, we note that our version of the `Range` class has implicit
# support for iteration, due to its explicit support of both `__len__` and `__getitem__`.
# The class also receives implicit support of the Boolean test, "`k **in** r`" for Range
# r. This test is evaluated based on a forward iteration through the range, as evidenced
# by the relative quickness of the test `2` **`in`** `Range(10000000)` versus `9999999`
# **`in`** `Range(10000000)`. Provide a more efficient implementation of the
# `__contains__` method to determine whether a particular value lies within a given
# range. The running time of your method should be independent of the length of the
# range.

from time import time_ns

class Range:
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

  def __contains__(self, n):
    """Returns True if n exists in Range, else False."""
    return (n - self._start) % self._step == 0

if __name__ == "__main__":
  r = Range(0, 10000, 2)
  start = time_ns()
  2 in r
  stop = time_ns()
  print(stop - start)   # 0 ns with overloaded __contains__, 0 ns without
  start = time_ns()
  99999 in r
  stop = time_ns()
  print(stop - start)   # 0 ns witt overloaded __contains__, 10,089,100 ns without