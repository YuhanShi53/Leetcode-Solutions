""" Leetcode 274 - H-Index

https://leetcode.com/problems/h-index/

1. SM Iteration: Time: O(nlogn) Space: O(1) (n is num of papers)
2. Bucket-Sort: Time: O(n) Space: O(n) (n is num of papers)

"""

from typing import List


class Solution1:
    """ 1. Iteration """

    def h_index(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        count = 0
        h_index = 0
        for x in citations:
            count += 1
            if count <= x:
                h_index = count
        return h_index


class Solution2:
    """ 2. Bucket-Sort """

    def h_index(self, citations):
        num_papers = len(citations)
        bucket = [0 for i in range(num_papers+1)]
        for x in citations:
            if x >= num_papers:
                bucket[num_papers] += 1
            else:
                bucket[x] += 1

        count = 0
        for x in range(num_papers, -1, -1):
            count += bucket[x]
            if count >= x:
                return x


if __name__ == '__main__':
    citations = [3, 0, 6, 1, 5]
    h_index = Solution2().h_index(citations)
    print(h_index)
