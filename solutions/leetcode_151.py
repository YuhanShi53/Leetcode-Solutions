""" Leetcode 151 - Reverse Words in a String

https://leetcode.com/problems/reverse-words-in-a-string/

1. self-implement Normal-String-Manipulate: Time: 36(45%) Memory: 14MB(29%)

"""


class Solution1:
    """ 1. self-implement Normal-String-Manipulate """
    def reverse_words(self, s: str) -> str:
        words = s.split()
        reversed_words = ' '.join(words[::-1])
        return reversed_words


if __name__ == '__main__':
    s = '  hello world!  '
    reversed_s = Solution1().reverse_words(s)
    print(reversed_s)