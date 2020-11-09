""" Leetcode 1286 - Iterator of Combination

https://leetcode.com/problems/iterator-for-combination/


1. SM Pointer: Time: O(k) Space: O(k) (k is combination length)

"""


class CombinationIterator:
    """ 1. SM Pointer"""

    def __init__(self, characters: str, combinationlength: int):
        self.characters = characters
        self.length = combinationlength
        self.idx = [i for i in range(combinationlength)]
        self.max_idx = [
            i for i in
            range(len(characters)-combinationlength, len(characters))]
        self.has_next = True

    def next(self) -> str:
        res = []
        for i in self.idx:
            res.append(self.characters[i])
        res = ''.join(res)

        add_one = 1
        for i in range(self.length-1, -1, -1):
            self.idx[i] += add_one
            add_one = 1 if self.idx[i] > self.max_idx[i] else 0

        if self.idx[0] > self.max_idx[0]:
            self.has_next = False
        else:
            for i in range(self.length):
                if self.idx[i] > self.max_idx[i]:
                    self.idx[i] = self.idx[i - 1] + 1

        return res

    def hasNext(self) -> bool:
        return self.has_next


if __name__ == '__main__':
    characters = 'abc'
    length = 2
    x = CombinationIterator(characters, length)
    print(x.next())
    print(x.hasNext())
    print(x.next())
    print(x.hasNext())
    print(x.next())
    print(x.hasNext())
