from typing import List


class Solution1:
    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i, s in enumerate(order):
            order_dict[s] = i
        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if j == len(words[i]) or order_dict[words[i-1][j]] > order_dict[words[i][j]]:
                    return False
                if order_dict[words[i-1][j]] < order_dict[words[i][j]]:
                    break
        return True


class Solution2:
    """ Simplified of Solution1 

    Borrow from: https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order

    """

    def is_alien_sorted(self, words, order):
        order_dict = {s: i for i, s in enumerate(order)}
        words = [[order_dict[x] for x in word] for word in words]
        return all(word1 < word2 for word1, word2 in zip(words, words[1:]))


if __name__ == '__main__':
    words = ["word"]
    order = 'worldabcefghijkmnpqstuvxyz'
    ans = Solution1().is_alien_sorted(words, order)
    print(ans)
