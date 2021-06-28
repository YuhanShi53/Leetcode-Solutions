""" Leetcode 916 - Word Subsets

https://leetcode.com/problems/word-subsets/

1. Time: O(M+N) Memory: O(26) (M+N are total number of characters in A and B)
2. Time: O(M+N) Memory: O(26) (M+N are total number of characters in A and B)

"""

from typing import List


class Solution1:
    """ 1. MINE | Hashmap """

    def word_subsets(self, A: List[str], B: List[str]) -> List[str]:

        def count(word):
            count_list = [0] * 26
            for x in word:
                count_list[ord(x)-97] += 1
            return count_list

        word_list = [0] * 26
        for word in B:
            for i, x in enumerate(count(word)):
                word_list[i] = max(word_list[i], x)

        subsets = []
        for word in A:
            count_word_a = count(word)
            flag = True
            for x, y in zip(count_word_a, word_list):
                if y - x > 0:
                    flag = False
            if flag:
                subsets.append(word)

        return subsets


class Solution2:
    """ 2. Simplified of 1

    Borrow from: https://leetcode.com/problems/word-subsets/discuss/175854/JavaC%2B%2BPython-Straight-Forward

    """

    def word_subsets(self, A, B):
        from collections import Counter
        pattern = Counter([])
        for word in B:
            pattern |= Counter(word)
        return [a for a in A if Counter(a) & pattern == pattern]


if __name__ == '__main__':
    A = ["amazon", "apple", "facebook", "google", "leetcode"]
    B = ["lo", "eo"]
    ans = Solution1().word_subsets(A, B)
    print(ans)
