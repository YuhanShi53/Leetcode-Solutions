from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.val = 0


class MapSum:

    def __init__(self):
        self._root = TrieNode()
        self._dict = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self._dict[key]
        self._dict[key] = val
        current = self._root
        for x in key:
            current = current.child[x]
            current.val += diff

    def sum(self, prefix: str) -> int:
        current = self._root
        for x in prefix:
            if x not in current.child:
                return 0
            current = current.child[x]
        return current.val
