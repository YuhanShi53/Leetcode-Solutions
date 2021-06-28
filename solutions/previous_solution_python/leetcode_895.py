""" Leetcode 895 - Maximum Frequency Stack

https://leetcode.com/problems/maximum-frequency-stack/

1. Time: O(n) Memory: O(n) (n is number of unique value pushed in stack)
2. Time: O(1) Memory: O(n) (n is number of unique value pushed in stack)

"""


class FreqStack1:
    """ 1. MINE | Hash Map | Stack """

    def __init__(self):
        self._counter = {}
        self._stack = []

    def push(self, x: int) -> None:
        self._counter[x] = self._counter.get(x, 0) + 1
        self._stack.append(x)

    def pop(self) -> int:
        max_frequency = max(self._counter.values())
        i = len(self._stack) - 1
        while i >= 0:
            if self._counter[self._stack[i]] == max_frequency:
                res = self._stack[i]
                self._counter[res] -= 1
                self._stack = self._stack[:i] + self._stack[i+1:]
                return res
            i -= 1


class FreqStack2():
    """ 2. Stack | Hash Map

    Borrow from https://leetcode.com/problems/maximum-frequency-stack/discuss/163410/C%2B%2BJavaPython-O(1)

    """

    def __init__(self):
        self._counter = {}
        self._stack = {}
        self._max_frequency = 0

    def push(self, x):
        self._counter[x] = self._counter.get(x, 0) + 1
        self._max_frequency = max(self._max_frequency, self._counter[x])
        if not self._stack.get(self._counter[x], False):
            self._stack[self._counter[x]] = []
        self._stack[self._counter[x]].append(x)

    def pop(self):
        res = self._stack[self._max_frequency].pop()
        self._counter[res] -= 1
        if not self._stack[self._max_frequency]:
            self._max_frequency -= 1
        return res


if __name__ == '__main__':
    stack = FreqStack2()
    stack.push(5)
    stack.push(7)
    stack.push(5)
    stack.push(7)
    stack.push(4)
    stack.push(5)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
