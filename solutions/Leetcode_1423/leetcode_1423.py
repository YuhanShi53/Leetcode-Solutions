from typing import List


class Solution1:
    def max_score(self, cardPoints: List[int], k: int) -> int:
        length = len(cardPoints)
        if k >= length:
            return sum(cardPoints)
        maximum_score = score = sum(cardPoints[:k])
        for i in range(-1, -k-1, -1):
            score = score - cardPoints[k+i] + cardPoints[i]
            maximum_score = max(maximum_score, score)
        return maximum_score


if __name__ == '__main__':
    nums = [1, 100, 1]
    k = 1
    ans = Solution1().max_score(nums, k)
    print(ans)
