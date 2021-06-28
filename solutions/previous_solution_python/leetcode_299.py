""" Leetcode 299 - Bulls and Cows

https://leetcode.com/problems/bulls-and-cows/

1. MINE Dict: Time: O(n) Space: O(n) (n is len_nums)

"""

from collections import defaultdict


class Solution1:
    """ 1. MINE Dict"""

    def get_hint(self, secret: str, guess: str) -> str:
        a_count = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                a_count += 1

        num_dict = defaultdict(int)
        for x in secret:
            num_dict[x] += 1
        b_count = 0
        for x in guess:
            if num_dict[x]:
                num_dict[x] -= 1
                b_count += 1
        b_count -= a_count

        return '{}A{}B'.format(a_count, b_count)


if __name__ == '__main__':
    secret = '1888'
    guess = '8881'
    res = Solution1().get_hint(secret, guess)
    print(res)
