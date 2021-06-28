# https://leetcode.com/problems/largest-triangle-area/submissions/
# Time:26.45% Memory:100%

class Solution(object):
    def largest_triangle_area(self, points):
        max_area = 0
        for i in range(len(points) - 2):
            for j in range(i+1, len(points) - 1):
                for k in range(j+1, len(points)):
                    three_points = [points[i], points[j], points[k]]
                    area = self.calculate_triangle_area(three_points)
                    if max_area < area:
                        max_area = area
        return max_area

    def calculate_triangle_area(self, points):
        xs = [point[0] for point in points] + [points[0][0]]
        ys = [point[1] for point in points] + [points[0][1]]
        area = 0
        for i in range(3):
            area += xs[i] * ys[i + 1]
            area -= ys[i] * xs[i + 1]
        area = abs(area) /  2.0
        return area

if __name__ == "__main__":
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    area = Solution().largest_triangle_area(points)
    print(area)


        