class Solution1:
    def halves_are_alike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        half_len = len(s) // 2
        num_l, num_r = 0, 0
        for i in range(half_len):
            num_l += s[i] in vowels
            num_r += s[i+half_len] in vowels
        return num_l == num_r


if __name__ == '__main__':
    s = "AbCdEfGh"
    ans = Solution1().halves_are_alike(s)
    print(ans)
