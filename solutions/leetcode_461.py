""" Leetcode 461 - Hamming Distance

https://leetcode.com/problems/hamming-distance/

1. self-implement: Time: 28ms(77%) Memory: 14MB(13%)
2. bit manipulate: Time: 32ms(51%) Memory: 13.9MB(22%)

"""

class Solution1:
    """ 1. self-implement """
    def hamming_distance(self, x, y):
        return bin(x ^ y).count('1')

class Solution2:
    """ 2. bit manipulate """
    def hamming_distance(self, x, y):
        x ^= y
        count = 0
        while x:
            x &= x - 1
            count += 1
        return count

if __name__ == '__main__':
    x = 7
    y = 4
    hamming_distance = Solution1().hamming_distance(x, y)
    print(hamming_distance)