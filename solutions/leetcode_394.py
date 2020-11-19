""" Leetcode 394 - Decode string

https://leetcode.com/problems/decode-string/

1. Time: O(N) Memory: O(N) (N is length of string)

"""


class Solution1:
    """ 1. MINE-Stack """

    def decode_string(self, s: str) -> str:
        factors = []
        substrings = ['']
        factor = ''
        for x in s:
            if x.isdigit():
                factor += x
            elif x == '[':
                factors.append(int(factor))
                substrings.append('')
                factor = ''
            elif x == ']':
                substrings[-1] += factors.pop() * substrings.pop()
            else:
                substrings[-1] += x
        return substrings.pop()


class Solution2:
    """ 2. Recursive """

    def decode_string(self, s: str) -> str:
        pass


if __name__ == '__main__':
    s = 'a'
    decoded_s = Solution1().decode_string(s)
    print(decoded_s)
