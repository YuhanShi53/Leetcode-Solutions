from collections import defaultdict
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        directions = {}
        succ_probs = defaultdict(list)
        for i, (x, y) in enumerate(edges):
            directions[x] = directions.get(x, []) + [y]
            directions[y] = directions.get(y, []) + [x]
            succ_probs[x].append(succProb[i])
            succ_probs[y].append(succProb[i])
        res = self.bfs(start, end, [start], directions, succ_probs, 1.0)
        return res
        
    def bfs(self, start, end, visited, directions, succ_probs, prob):
        res = []
        for i, x in enumerate(directions.get(start)):
            if x in visited:
                res.append(0.0)
            elif x == end:
                res.append(prob * succ_probs[start][i])
            else:
                res.append(self.bfs(x, end, visited+[x], directions, succ_probs, prob*succ_probs[start][i]))
        return max(res)
            

if __name__ == '__main__':
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succ_probs = [0.5, 0.5, 0.2]
    start = 0
    end = 2
    res = Solution().maxProbability(n, edges, succ_probs, start, end)
    print(res)