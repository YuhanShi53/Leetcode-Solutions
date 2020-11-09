""" Leetcode 547 - Friend Circles

https://leetcode.com/problems/friend-circles/

1. Union-Find: Time: O(n^2) Space: O(n)
2. DFS: Time: O(n^2) Space: O(n)

"""

from typing import List


class Solution1:
    """ 1. Union-Find """

    def find_circle_num(self, M):
        num_students = len(M)
        count = num_students
        fathers = [i for i in range(num_students)]

        def find_father(x):
            father = x
            while father != fathers[father]:
                father = fathers[father]

            while x != father:
                temp = fathers[x]
                fathers[x] = father
                x = temp
            return father

        def union_two_circle(x, y):
            nonlocal count
            father_x = find_father(x)
            father_y = find_father(y)
            if father_x != father_y:
                fathers[father_x] = father_y
                count -= 1

        for i in range(num_students):
            for j in range(i+1, num_students):
                if M[i][j]:
                    union_two_circle(i, j)

        return count


class Solution2:
    """ 2. DFS """

    def find_circle_num(self, M):
        is_row_visited = [False] * len(M)
        friends_in_circle = []
        num_circles = 0
        for i, row in enumerate(M):
            if not is_row_visited[i]:
                friends_in_circle = {i}
                num_circles += 1

            while len(friends_in_circle) > 0:
                j = friends_in_circle.pop()
                is_row_visited[j] = True
                for k in range(i+1, len(row)):
                    if M[j][k] == 1 and not is_row_visited[k]:
                        friends_in_circle.add(k)
        return num_circles


if __name__ == "__main__":
    M = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    res = Solution1().find_circle_num(M)
    print(res)
