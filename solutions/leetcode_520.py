""" Leetcode 520 - Detect Capital

https://leetcode.com/problems/detect-capital/

1. MINE Naive: Time: O(n) Space: O(1)

"""


class Solution1:
    """ 1. MINE """

    def detect_capital_use(self, word: str) -> bool:
        is_first_capital = True if word[0].isupper() else False
        num_capital = 0
        for x in word:
            if x.isupper():
                num_capital += 1

        if (num_capital == 0 or num_capital == len(word)
                or num_capital == 1 and is_first_capital):
            return True
        return False


if __name__ == '__main__':
    word = 'FlaG'
    res = Solution1().detect_capital_use(word)
    print(res)
