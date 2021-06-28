""" Leetcode 797 - All Paths From Source To Target

https://leetcode.com/problems/all-paths-from-source-to-target/


1. MINE DFS: Time: O(2^(N-2)) Space: O((N+2)*2^(N-3))

"""

from typing import List


class Solution1:
    """ 1. MINE DFS """

    def all_paths_source_target(self, graph: List[List[int]]) -> List[List[int]]:
        if not graph:
            return []

        paths = []
        target_idx = len(graph) - 1
        self.dfs(graph, 0, target_idx, [], paths)
        return paths

    def dfs(self, graph, idx, target_idx, path, all_paths):

        if idx == target_idx:
            all_paths.append(path+[idx])
            return

        if not graph[idx] and idx != target_idx:
            return

        for i in graph[idx]:
            self.dfs(graph, i, target_idx, path+[idx], all_paths)


if __name__ == '__main__':
    graph = [[1, 2], [3], [3], []]
    res = Solution1().all_paths_source_target(graph)
    print(res)
