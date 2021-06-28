""" Leetcode 3 - Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/

1. Time: O(n) Memory: O(26) (n is length of s, 26 is number of Alphabet)

"""


class Solution1:
    """ 1. MINE | Hash """

    def length_of_longest_substring(self, s: str) -> int:
        num_dict = {}
        i, j = -1, 0
        max_length = 0
        while j < len(s):
            if num_dict.get(s[j], None) is not None:
                i = max(num_dict[s[j]], i)
            max_length = max(max_length, j - i)
            num_dict[s[j]] = j
            j += 1
        return max_length


if __name__ == '__main__':
    s = ''
    res = Solution1().length_of_longest_substring(s)
    print(res)
