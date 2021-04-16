class Solution1:
    def remove_duplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        ans = []
        for x in s:
            if not ans or x != ans[-1][0]:
                ans.append([x, 1])
            elif ans[-1][1] + 1 == k:
                ans.pop()
            else:
                ans[-1][1] += 1
        ret = ''.join([char * count for char, count in ans])
        return ret


if __name__ == '__main__':
    s = 'abcd'
    k = 2
    ans = Solution1().remove_duplicates(s, k)
    print(ans)
