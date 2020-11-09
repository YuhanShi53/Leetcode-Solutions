""" Leetcode 190 - Reverse Bits 

https://leetcode.com/problems/reverse-bits/

1. Basic implement: Time: 32ms(68%) Memory: 14MB(9.5%)

"""

class Solution1:
    """ 1. Basic implement """
    def reverse_bits(self, n: int) -> int:
        bits = bin(n)[2:]
        reversed_n = int(bits[::-1] + '0'*(32-len(bits)), 2)
        return reversed_n

if __name__ == '__main__':
    n = 43261596
    print('previous: {}'.format(bin(n)[2:]))
    reversed_n = Solution1().reverse_bits(n)
    print('reversed: {}'.format(bin(reversed_n)[2:]))
    