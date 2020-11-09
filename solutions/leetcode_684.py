""" Leetcode 684 - Redundant Connection

https://leetcode.com/problems/redundant-connection/

1. SM Union-Find: Time: O(n) Space: O(n) (n is num of nodes)

"""


from typing import List


class Solution1():
    """ 1. SM Union-Find """

    def find_redundant_connection(self, edges: List[List[int]]) -> List[int]:
        relations = [i for i in range(len(edges) + 1)]

        def find(x):
            while relations[x] != x:
                relations[x] = relations[relations[x]]
                x = relations[x]
            return x

        for x, y in edges:
            x_parent = find(x)
            y_parent = find(y)
            if x_parent != y_parent:
                if x_parent <= y_parent:
                    relations[y_parent] = x_parent
                else:
                    relations[x_parent] = y_parent
            else:
                return [x, y]


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    res = Solution1().find_redundant_connection(edges)
    print(res)
