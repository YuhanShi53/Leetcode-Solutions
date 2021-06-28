""" Leetcode 647 - Palindromic Substring

https://leetcode.com/problems/palindromic-substrings/

1. Time: O(n^2) Memory: O(1) (n is length string)

"""


class Solution1:
    """ 1. Dynamic Praogramming 

    Borrow from: https://leetcode.com/problems/palindromic-substrings/discuss/105689/Java-solution-8-lines-extendPalindrome

    """

    def count_substrings(self, s: str) -> int:

        count = 0

        def extend(j, k):
            nonlocal count
            max_extend = min(j+1, len(s)-k)
            while j >= 0 and k < len(s) and s[j] == s[k]:
                count += 1
                j -= 1
                k += 1

        for i in range(len(s)):
            extend(i, i)
            extend(i, i+1)
        return countx


if __name__ == '__main__':
    s = 'aaabefaaa'
    ans = Solution1().count_substrings(s)
    print(ans)
