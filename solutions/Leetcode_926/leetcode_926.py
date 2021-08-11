class Solution1:
    def min_flips_mono_incr(self, s):
        min_flip = 0
        num_ones = 0
        for x in s:
            if x == '0':
                min_flip = min(num_ones, min_flip+1)
            else:
                num_ones += 1
        return min_flip


class SolutionMINE:
    def min_flips_mono_incr(self, s: str) -> int:
        num_left_flip = 0
        num_right_flip = s.count('0')
        min_flip = num_left_flip + num_right_flip
        current = min_flip
        for x in s:
            current += 1 if x == '1' else -1
            min_flip = min(min_flip, current)
        return min_flip
