""" Leetcode 284 - Peeking Iterator

https://leetcode.com/problems/peeking-iterator/

"""


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self._iterator = iterator
        self._next = iterator.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self._next

    def next(self):
        """
        :rtype: int
        """
        res = self._next
        self._next = self._iterator.next() if self._iterator.hasNext() else None
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._next is not None
