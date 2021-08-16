from collections import defaultdict


class Solution1:
    def min_windows(self, s, t):
        char_count = defaultdict(int)
        for x in t:
            char_count[x] += 1
        missing = len(t)
        left = right = 0
        min_substring = ''
        min_len = len(s)
        while right < len(s):
            if char_count.get(s[right], 0) > 0:
                missing -= 1
            char_count[s[right]] -= 1
            right += 1
            while missing == 0:
                if right - left <= min_len:
                    min_len = right - left
                    min_substring = s[left:right]
                if char_count.get(s[left], 0) == 0:
                    missing += 1
                char_count[s[left]] += 1
                left += 1
        return min_substring


class SolutionMINE:
    def min_windows(self, s: str, t: str) -> str:
        def is_substring(s_count, t_count):
            for x, y in zip(s_count, t_count):
                if y > x:
                    return False
            return True

        t_count = [0] * 58
        for x in t:
            t_count[ord(x) - 65] += 1
        substring_count = [0] * 58
        min_substring = ''
        left = 0
        right = -1
        len_s = len(s)
        while left < len(s):
            if not is_substring(substring_count, t_count):
                if right == len_s - 1:
                    return min_substring
                right += 1
                substring_count[ord(s[right]) - 65] += 1
            else:
                substring_count[ord(s[left]) - 65] -= 1
                left += 1
            if is_substring(substring_count, t_count) and (not min_substring or right - left + 1 < len(min_substring)):
                min_substring = s[left:right+1]
        return min_substring
