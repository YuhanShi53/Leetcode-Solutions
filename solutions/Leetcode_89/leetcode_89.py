from typing import List


class Solution1:
    def gray_code(self, n: int) -> List[int]:
        ret = [0]
        for k in range(n):
            ret += [x | (1 << k) for x in reversed(ret)]
        return ret
