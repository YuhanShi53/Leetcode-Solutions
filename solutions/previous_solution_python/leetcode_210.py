""" Leetcode 210 - Course Schedule II

https://leetcode.com/problems/course-schedule-ii/

1. Topological-Sorting & BFS: Time: O(E+V) Space: O(E+V)

"""

from typing import List


class Solution1:
    """ 1. Topological Sorting & BFS """

    def find_order(self, numCourses: int,
                   prerequisites: List[List[int]]) -> List[int]:

        if numCourses == 1:
            return [0]

        out_dict = {}
        in_dict = {}
        for x in range(numCourses):
            in_dict[x] = 0

        for pair in prerequisites:
            if out_dict.get(pair[0], 0):
                out_dict[pair[0]].append(pair[1])
            else:
                out_dict[pair[0]] = [pair[1]]
            in_dict[pair[1]] += 1

        courses_without_in = []
        order = []
        for item in in_dict.items():
            if item[1] == 0:
                courses_without_in.append(item[0])

        while courses_without_in:
            course_no_pre = courses_without_in.pop()
            order.append(course_no_pre)

            for x in out_dict.get(course_no_pre, []):
                in_dict[x] -= 1
                if in_dict[x] == 0:
                    courses_without_in.insert(0, x)

        return order[::-1] if len(order) == numCourses else []


if __name__ == '__main__':
    num_courses = 3
    prerequisites = [[0, 1], [0, 2], [1, 2]]
    res = Solution1().find_order(num_courses, prerequisites)
    print(res)
