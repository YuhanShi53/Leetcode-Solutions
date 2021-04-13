class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        raise NotImplementedError

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        raise NotImplementedError

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        raise NotImplementedError


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self._stack = [[nestedList, 0]]

    def next(self) -> int:
        level, id = self._stack[-1]
        self._stack[-1][1] += 1
        return level[id].getInteger()

    def hasNext(self) -> bool:
        while self._stack:
            level, id = self._stack[-1]
            if id >= len(level):
                self._stack.pop()
            else:
                if level[id].isInteger():
                    return True
                self._stack[-1][1] += 1
                self._stack.append([level[id].getList(), 0])
        return False
