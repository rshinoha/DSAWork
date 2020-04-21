# Data Structures and Algorithms in Python Ch.2 (Goodrich et. al.)
# Creativity exercise C-2.26
# Ryoh Shinohara
# =======================================================================================
# **C-2.26**  The `SequenceIterator` class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named `ReversedSequenceIterator` that serves as a
# reverse iterator for any Python sequence type. The first call to next should return the
# last element of the sequence, the second call to next should return the second-to-last
# element, and so forth.

class ReversedSequenceIterator:
    """A reverse iterator for any of Python's sequence type"""
    def __init__(self, sequence):
        """Create an iterator for a given sequence"""
        self._sequence = sequence
        self._k = len(sequence)         # Will decrement on first call
    
    def __next__(self):
        """Return the next element, or else raise StopIteration error."""
        self._k -= 1
        if self._k > -1:
            return(self._sequence[self._k])
        else:
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

if __name__ == "__main__":
    seq = [1,3,5,7,9]
    revSeq = ReversedSequenceIterator(seq)
    for i in range(len(seq)):
        print(next(revSeq))