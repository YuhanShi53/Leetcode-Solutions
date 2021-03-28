""" Leetcode 423 - Reconstruct Original Digits From English

https://leetcode.com/problems/reconstruct-original-digits-from-english/

1. Time: O(n) Memory: O(1) (n is length of s)
2. Time: O(n) Memory: O(1) (n is length of s)

"""


class Solution1:
    """ 1. MINE | Hashmap """

    def original_digits(self, s: str) -> str:
        digit_chars = [
            (('z', 1), ('e', 1), ('r', 1), ('o', 1)),
            (('o', 1), ('n', 1), ('e', 1)),
            (('t', 1), ('w', 1), ('o', 1)),
            (('t', 1), ('h', 1), ('r', 1), ('e', 2)),
            (('f', 1), ('o', 1), ('u', 1), ('r', 1)),
            (('f', 1), ('i', 1), ('v', 1), ('e', 1)),
            (('s', 1), ('i', 1), ('x', 1)),
            (('s', 1), ('e', 2), ('v', 1), ('n', 1)),
            (('e', 1), ('i', 1), ('g', 1), ('h', 1), ('t', 1)),
            (('n', 2), ('i', 1), ('e', 1))
        ]

        temp_2 = [('z', 0), ('w', 2), ('u', 4), ('f', 5), ('x', 6),
                  ('s', 7), ('g', 8), ('i', 9), ('o', 1), ('h', 3)]

        ans = [''] * 10
        char_count = [0] * 26
        for x in s:
            char_count[ord(x) - 97] += 1

        for key, value in temp_2:
            count = char_count[ord(key) - 97]
            for k, num in digit_chars[value]:
                char_count[ord(k) - 97] -= count * num
            ans[value] = count * str(value)
        return ''.join(ans)


class Solution2:
    """ 2. Straight-Forward

    Borrow from: https://leetcode.com/problems/reconstruct-original-digits-from-english/discuss/91207/one-pass-O(n)-JAVA-Solution-Simple-and-Clear

    """

    def original_digits(self, s):
        count = [0] * 10
        for x in s:
            if x == 'z':
                count[0] += 1
            elif x == 'n':
                count[1] += 1  # 1 + 7 + 2 * 9
            elif x == 'w':
                count[2] += 1
            elif x == 'h':
                count[3] += 1  # 3 + 8
            elif x == 'u':
                count[4] += 1
            elif x == 'f':
                count[5] += 1  # 4 + 5
            elif x == 'x':
                count[6] += 1
            elif x == 's':
                count[7] += 1  # 6 + 7
            elif x == 'g':
                count[8] += 1
            elif x == 'i':
                count[9] += 1  # 9 + 8 + 6 + 5

        count[3] -= count[8]
        count[5] -= count[4]
        count[7] -= count[6]
        count[9] -= (count[8] + count[6] + count[5])
        count[1] -= (count[7] + 2 * count[9])

        ans = ''
        for i in range(10):
            ans += str(i) * count[i]
        return ans


if __name__ == '__main__':
    s = "zeroonetwothreefourfivesixseveneightnine"
    ans = Solution2().original_digits(s)
    print(ans)
