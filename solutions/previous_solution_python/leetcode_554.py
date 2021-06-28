# https://leetcode.com/problems/brick-wall/submissions/ 
# Time:90% Space:50%

class Solution:
    def leastBricks(self, wall):
        brick_length_in_row_statistics = {}
        total_length = sum(wall[0])
        for row in wall:
            brick_length = 0
            for brick in row:
                brick_length += brick
                if brick_length < total_length:
                    if brick_length_in_row_statistics.get(brick_length, 0):
                        brick_length_in_row_statistics[brick_length] += 1
                    else:
                        brick_length_in_row_statistics[brick_length] = 1

        num_most_popular_length = 0
        for brick_length in brick_length_in_row_statistics.values():
            if brick_length > num_most_popular_length:
                num_most_popular_length = brick_length
        num_cross_bricks = len(wall) - num_most_popular_length
        return num_cross_bricks


if __name__ == "__main__":
    wall = [[1, 2, 2, 1], [3, 1, 2], [1, 3, 2],
            [2, 4], [3, 1, 2], [1, 3, 1, 1]]
    res = Solution().leastBricks(wall)
    print(res)
