import math


class Solution1:
    def judge_sqaure_sum(c: int) -> bool:
        m = math.floor(math.sqrt(c))
        n = 0
        while m >= n:
            current = m**2 + n ** 2
            if current == c:
                return True
            if current < c:
                n += 1
            else:
                m -= 1
        return False
