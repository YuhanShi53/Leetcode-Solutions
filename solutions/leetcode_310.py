""" Leetcode 310 - Minimum Height Trees

https://leetcode.com/problems/minimum-height-trees/

"""

from collections import defaultdict
from typing import List


class Solution1:
    """ 1. SM BFS """

    def find_min_height_trees(self, n: int, edges: List[List[int]]
                              ) -> List[int]:
        if n == 1:
            return [0]
        edge_dict = defaultdict(list)
        edge_num_of_node = defaultdict(int)
        for edge in edges:
            edge_dict[edge[0]].append(edge[1])
            edge_dict[edge[1]].append(edge[0])
            edge_num_of_node[edge[0]] += 1
            edge_num_of_node[edge[1]] += 1
        while edge_num_of_node:

            leaves = []
            for node_id, edge_num in edge_num_of_node.items():
                if edge_num <= 1:
                    leaves.append(node_id)

            for node in leaves:
                for linked_node in edge_dict[node]:
                    if linked_node in edge_num_of_node:
                        edge_num_of_node[linked_node] -= 1
                edge_num_of_node.pop(node)
        return leaves


if __name__ == '__main__':
    n = 6
    edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
    roots = Solution1().find_min_height_trees(n, edges)
    print(roots)
