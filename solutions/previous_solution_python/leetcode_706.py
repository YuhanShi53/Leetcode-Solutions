""" Leetcode 706 - Design Hashmap

https://leetcode.com/problems/design-hashmap/

"""


class MyHashMap1:
    """ 1. MINE | Pure-Array """

    def __init__(self):
        self._map = [None for i in range(1000000)]

    def put(self, key: int, value: int):
        self._map[key] = value

    def get(self, key: int):
        return self._map[key] if self._map[key] is not None else -1

    def remove(self, key: int):
        self._map[key] = None


class LinkedList:
    def __init__(self, key, value):
        self.pair = [key, value]
        self.next = None


class MyHashMap2:
    """ 2. Array with Linked List """

    def __init__(self):
        self._length = 1000
        self._array = [None for i in range(self._length)]

    def put(self, key, value):
        id = key % self._length
        if self._array[id] is None:
            self._array[id] = LinkedList(key, value)
        else:
            head = self._array[id]
            while True:
                if head.pair[0] == key:
                    head.pair[1] = value
                    return
                if head.next is None:
                    break
                head = head.next
            head.next = LinkedList(key, value)

    def get(self, key):
        id = key % self._length
        head = self._array[id]
        while head:
            if head.pair[0] == key:
                return head.pair[1]
            head = head.next
        return -1

    def remove(self, key):
        id = key % self._length
        if self._array[id] is None:
            return
        if self._array[id].pair[0] == key:
            self._array[id] = self._array[id].next
            return
        head = self._array[id]
        while head.next:
            if head.next.pair[0] == key:
                head.next = head.next.next
                return
            head = head.next
