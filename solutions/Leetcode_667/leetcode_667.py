from typing import List


class Solution1:
    def construct_array(self, n: int, k: int) -> List[int]:
        array = [1]
        factor = 1
        for d in range(n-1, n-k, -1):
            array.append(array[-1] + factor * d)
            factor *= -1
        for _ in range(n-k):
            array.append(array[-1] + factor)
        return array


class Solution2:
    def construct_array(self, n, k):
        array = []
        i, j = 1, n
        while i <= j:
            if k > 1:
                if k % 2:
                    array.append(i)
                    i += 1
                else:
                    array.append(j)
                    j -= 1
                k -= 1
            else:
                array.append(i)
                i += 1
        return array


if __name__ == '__main__':
    n = 3
    k = 2
    ans = Solution1().construct_array(n, k)
    print(ans)
