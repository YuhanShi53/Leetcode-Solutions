""" Leetcode 1641 - Count Sorted Vowel Strings

https://leetcode.com/problems/count-sorted-vowel-strings/

1. Time: O(n) Memory: O(1)
2. Time: O(n) Memory: O(n)
3. Time: O(1) Memory: O(1)

"""


from itertools import accumulate


class Solution1:
    """ 1. MINE | Math | Dynamic Programming """

    def count_vowel_strings(self, n: int) -> int:
        counts = [1, 0, 0, 0, 0]
        for x in range(n - 1):
            for i in range(1, 5):
                counts[i] = counts[i] + counts[i-1]
        total = 0
        for x, count in zip([5, 4, 3, 2, 1], counts):
            total += x * count
        return total


class Solution2:
    """ 2. Simplified of 1

    https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC%2B%2BPython-DP-O(1)-Time-and-Space

    """
    from itertools import accumulate

    def count_vowel_strings(self, n):
        counts = [1] * 5
        for i in range(n):
            counts = accumulate(counts)
        return list(counts)[-1]


class Solution3:
    """ 3. Math

    https://leetcode.com/problems/count-sorted-vowel-strings/discuss/918498/JavaC%2B%2BPython-DP-O(1)-Time-and-Space

    """

    def count_vowel_strings(self, n):
        return (n + 1) * (n + 2) * (n + 3) * (n + 4) // 24


if __name__ == '__main__':
    n = 33
    res = Solution3().count_vowel_strings(n)
    print(res)
