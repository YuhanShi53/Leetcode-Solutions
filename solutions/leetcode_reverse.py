import re

class Solution:
    def reverse_words(self, s):
        word_list = re.split(r" +", s.strip())
        reverse_word_list = word_list[::-1]
        reversed_words = " ".join(reverse_word_list)
        return reversed_words

if __name__ == "__main__":
    s = "  hello world!  "
    reversed_s = Solution().reverse_words(s)
    print(reversed_s)
        