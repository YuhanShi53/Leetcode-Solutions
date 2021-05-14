from typing import List


class Solution1:
    def ambiguous_coordinates(self, s: str) -> List[str]:
        s = s[1:len(s)-1]
        ans = []
        for split_id in range(1, len(s)):
            left, right = s[:split_id], s[split_id:]
            left_candidates = self.get_candidates(left)
            right_candidates = self.get_candidates(right)
            for left in left_candidates:
                for right in right_candidates:
                    ans.append('({}, {})'.format(left, right))
        return ans

    def get_candidates(self, s):
        """
        s = 'x' -> return ['x']
        s = '0' -> return []
        s = '0xxx0' -> return []
        s = '0xxx' -> return ['0.xxx']
        s = 'xxx0' -> return ['xxx0']
        s = 'xxx' -> return ['x.xx', 'xx.x', 'xxx']
        """
        if len(s) == 1:
            return [s]
        if s[0] == s[-1] == '0':
            return []
        if s[0] == '0':
            return ['0.' + s[1:]]
        if s[-1] == '0':
            return [s]
        return [s[:i] + '.' + s[i:] for i in range(1, len(s))] + [s]


if __name__ == '__main__':
    s = "(0123)"
    ans = Solution1().ambiguous_coordinates(s)
    print(ans)
