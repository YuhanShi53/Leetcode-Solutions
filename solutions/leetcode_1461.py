""" Leetcode 1461 - Check If A String Contains All Binary Codes of Size k

https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/


"""


class Solution1:
    """ 1. MINE | Set """

    def has_all_codes(self, s: str, k: int) -> bool:
        codes = set()
        for i in range(len(s) - k + 1):
            codes = codes.union({s[i:i+k]})
        return True if len(codes) == 2**k else False


if __name__ == '__main__':
    s = "00110"
    k = 2
    res = Solution1().has_all_codes(s, k)
    print(res)
