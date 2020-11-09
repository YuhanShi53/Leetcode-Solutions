""" Leetcode 58 - Length of Last Word

https://leetcode.com/problems/length-of-last-word/

1. SM Straight-Forward: Time: O(n) Space: O(1) (n is len_s)

"""


class Solution1:
    """ 1. SM Straight-Forward """

    def length_of_last_word(self, s: str) -> int:
        s = s.strip().split(' ')
        return len(s[-1])


if __name__ == '__main__':
    s = ' '
    res = Solution1().length_of_last_word(s)
    print(res)
