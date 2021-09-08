from typing import List


class Solution1:
    def shifting_letters(self, s: str, shifts: List[int]) -> str:
        prev_shift = 0
        ret = []
        for i in range(len(s)-1, -1, -1):
            total_shift = prev_shift + shifts[i]
            prev_shift = total_shift
            ret.append(chr((ord(s[i]) + total_shift - 97) % 26 + 97))
        return ''.join(ret[::-1])
