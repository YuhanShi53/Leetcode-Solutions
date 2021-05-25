class Solution1:
    def to_lower_case(self, s: str) -> str:
        return ''.join(chr(ord(x) + 32) if 65 <= ord(x) <= 90 else x for x in s)
        's'.islower


if __name__ == '__main__':
    s = 'LoVe&&ly'
    ans = Solution1().to_lower_case(s)
    print(ans)