""" Leetcode 824 - Goat Latin

https://leetcode.com/problems/goat-latin/


"""


class Solution1:
    """ 1. MINE """

    def to_goat_latin(self, S: str) -> str:
        s = S.split(' ')
        res = []
        vowel = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
        for i, x in enumerate(s):
            if x[0] in vowel:
                res.append(x + 'ma' + 'a' * (i+1))
            else:
                res.append(x[1:] + x[0] + 'ma' + 'a' * (i+1))
        return ' '.join(res)


if __name__ == '__main__':
    s = "I"
    res = Solution1().to_goat_latin(s)
    print(res)
