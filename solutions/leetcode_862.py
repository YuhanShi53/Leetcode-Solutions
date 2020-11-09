# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/submissions/
# Time: 94% Memory: 25%

import collections

class Solution:
    def shortest_subarray(self, A, K):
        accumulations = [0]
        for a in A:
            accumulations.append(accumulations[-1] + a)
        
        candidate_indices = collections.deque()
        shortest_length_of_subarray = len(A) + 1
        for i, accumulation in enumerate(accumulations):
            while candidate_indices and accumulations[candidate_indices[-1]] >= \
                accumulation:
                candidate_indices.pop()
            while candidate_indices and accumulation - accumulations[candidate_indices[0]] >= K:
                shortest_length_of_subarray = min(shortest_length_of_subarray, \
                    i-candidate_indices.popleft())
            candidate_indices.append(i)

        return shortest_length_of_subarray \
            if shortest_length_of_subarray < len(A) + 1 else -1

if __name__ == "__main__":
    A = [1]
    K = 1
    res = Solution().shortest_subarray(A, K)
    print(res)