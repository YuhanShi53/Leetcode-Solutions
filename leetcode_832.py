""" Leetcode 832 - Flipping an Image

https://leetcode.com/problems/flipping-an-image/

1. SM-Straight-Forward: Time: O(n) Space: O(1) (n is num of pixels)
2. One-Line-Straight-Forward: Time: O(n) Space: O(n) (n is num of pixels)

"""

import math
from typing import List


class Solution1:
    """ 1. SM-Straight-Forward """

    def flip_and_invert_image(self, image: List[List[int]]) -> List[List[int]]:
        width = len(image[0])
        mid = math.ceil(width / 2)
        for row in image:
            for i in range(mid):
                row[i], row[width-i-1] = (row[width-i-1] ^ 1, row[i] ^ 1)
        return image


class Solution2:
    """ 2. One-Line-Straight-Forward """

    def flip_and_invert_image(self, image):
        return [[x ^ 1 for x in row[::-1]] for row in image]


if __name__ == '__main__':
    image = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
    new_image = Solution2().flip_and_invert_image(image)
    print(new_image)
