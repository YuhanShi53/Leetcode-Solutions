""" Leetcode 705 - Design HashSet

https://leetcode.com/problems/design-hashset/

1. SM Naive: Time: O(1) Space: O(1000000)

"""


class MyHashSet:
    """ 1. SM Naive """

    def __init__(self):
        self.hashset = [False for i in range(1000000)]

    def add(self, key: int) -> None:
        self.hashset[key] = True

    def remove(self, key: int) -> None:
        self.hashset[key] = False

    def contains(self, key: int) -> bool:
        return self.hashset[key]


if __name__ == '__main__':
    key = 3
    obj = MyHashSet()
    obj.add(key)
    obj.remove(key)
    res = obj.contains(key)
    print(res)
