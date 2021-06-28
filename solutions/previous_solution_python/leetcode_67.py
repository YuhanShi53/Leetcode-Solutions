""" Leetcode 67 - Add Binary

https://leetcode.com/problems/add-binary/

1. self-implement: Time: 48ms(24%) Memory: 14MB(7%)
2. Simplified: Time: 44(31ms) Memory: 13.8MB(73%)

"""


class Solution1:
    """ 1. self-implement """
    def add_binary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        if b_len > a_len:
            a, b = b, a
            a_len, b_len = b_len, a_len

        b = '0' * (a_len - b_len) + b
        add_one = 0
        res = [0 for i in range(a_len)]
        for i in range(1, a_len + 1):
            temp = int(a[a_len - i]) + int(b[a_len - i]) + add_one
            if temp > 1:
                temp -= 2
                add_one = 1
            else:
                add_one = 0
            res[a_len - i] = str(temp)

        if add_one:
            res.insert(0, '1')
        return ''.join(res)


class Solution2:
    """ 2. Simplified """
    def add_binary(self, a, b):
        add_one = 0
        res = []
        a = list(a)
        b = list(b)

        while a or b or add_one:
            if a:
                add_one += int(a.pop())
            if b:
                add_one += int(b.pop())
            res.append(str(add_one % 2))
            add_one //= 2
        return ''.join(res[::-1])


if __name__ == '__main__':
    a = '1010'
    b = '1011'
    res = Solution2().add_binary(a, b)
    print(res)