from collections import defaultdict

class Solution:
    def remove_duplicate_letters(self, s):
        # encoded_s = [ord(x) for x in s]
        statistics_of_char = defaultdict(int)
        is_char_visit = defaultdict(bool)
        for x in s:
            statistics_of_char[x] += 1
            is_char_visit[x]
        res = ["0"]
        statistics_of_char["0"] = 1

        for x in s:
            statistics_of_char[x] -= 1

            if x in res:
                continue
            while x < res[-1] and statistics_of_char[res[-1]] > 0:
                res.pop()
            res.append(x)

        return "".join(res[1:])

        


if __name__ == "__main__":
    s = "ccacbaba"
    res = Solution().remove_duplicate_letters(s)
    print(res)