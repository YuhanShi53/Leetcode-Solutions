""" Leetcode 1344 - Angle Between Hands of a Clock

https://leetcode.com/problems/angle-between-hands-of-a-clock/

1. Self-implement: Time: 36ms(27%) Memory: 13.8MB(59%)

"""


class Solution1:
    """ 1. Self-implement """
    def angle_clock(self, hour: int, minutes: int) -> float:
        hour_angle = (hour % 12) * 30 + minutes / 60 * 30
        minute_angle = minutes * 6

        angle = abs(hour_angle - minute_angle)
        if angle > 180:
            angle = 360 - angle
        return angle


if __name__ == '__main__':
    hour = 0
    minutes = 0
    angle = Solution1().angle_clock(hour, minutes)
    print(angle)
