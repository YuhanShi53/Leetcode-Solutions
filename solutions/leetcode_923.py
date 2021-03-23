""" Leetcode 923- 3Sum With Multiplicity

https://leetcode.com/problems/3sum-with-multiplicity/

"""

from typing import List


class Solution1:
    """ 1. MINE """

    def three_sum_multi(self, arr: List[int], target: int) -> int:
        div = {1: 6, 2: 2, 3: 1}
        count_dict = {}
        for x in arr:
            count_dict[x] = count_dict.get(x, 0) + 1
        arr = sorted(list(set(arr)))
        count = 0
        for left in range(len(arr)):
            for right in range(left, len(arr)):
                temp = target - arr[left] - arr[right]
                if (not count_dict.get(temp, False)
                        or temp < arr[right]):
                    continue
                tup = (arr[left], arr[right], temp)
                time = 1
                count_dict_2 = count_dict.copy()
                for x in tup:
                    time *= count_dict_2[x]
                    count_dict_2[x] -= 1
                time //= div[len(set(tup))]
                count += time
        return int(count % (1e9 + 7))


if __name__ == '__main__':
    arr = [1, 1, 2, 2, 2, 2]
    target = 0
    res = Solution1().three_sum_multi(arr, target)
    print(res)
