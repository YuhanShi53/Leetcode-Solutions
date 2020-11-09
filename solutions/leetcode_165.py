""" Leetcode 165 - Compare Version Numbers

https://leetcode.com/problems/compare-version-numbers/

1. SM Straight-Forward: Time: O(n) Space: O(n) (n is len_longest_version)

"""


class Solution1:
    """ 1. SM Straight-Forward """

    def compare_version(self, version1: str, version2: str) -> int:
        num_1 = version1.split('.')
        num_2 = version2.split('.')

        if len(num_1) > len(num_2):
            num_2 += [0] * (len(num_1) - len(num_2))
        elif len(num_1) < len(num_2):
            num_1 += [0] * (len(num_2) - len(num_1))

        for x, y in zip(num_1, num_2):
            x = int(x)
            y = int(y)
            if x < y:
                return -1
            elif x > y:
                return 1
        return 0


if __name__ == '__main__':
    version_1 = '1.0.1'
    version_2 = '1'
    res = Solution1().compare_version(version_1, version_2)
    print(res)
