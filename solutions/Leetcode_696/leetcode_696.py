class Solution1:
    def count_binary_substrings(self, s: str) -> int:
        prev_count, current_count, total = 0, 0, 0
        prev = ''
        for x in s:
            if x != prev:
                total += min(prev_count, current_count)
                prev_count = current_count
                current_count = 1
                prev = x
            else:
                current_count += 1
        return total + min(current_count, prev_count)


if __name__ == '__main__':
    s = "0011001"
    ans = Solution1().count_binary_substrings(s)
    print(ans)
