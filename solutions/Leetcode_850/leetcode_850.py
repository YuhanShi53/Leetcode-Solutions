from typing import List


class Solution1:
    def rectangle_area(self, rectangles: List[List[int]]) -> int:
        xs = sorted(set(x for x1, y1, x2, y2 in rectangles for x in (x1, x2)))
        scan_line = [0] * len(xs)
        x_index = {x: i for i, x in enumerate(xs)}
        ys = []
        for x1, y1, x2, y2 in rectangles:
            ys.append((y1, x1, x2, 1))
            ys.append((y2, x1, x2, -1))
        ys.sort()
        yy = 0
        accumulate_x = 0
        area = 0
        for y, x1, x2, flag in ys:
            area += (y - yy) * accumulate_x
            yy = y
            for i in range(x_index[x1], x_index[x2]):
                scan_line[i] += flag
            accumulate_x = sum(x2 - x1 for x1, x2, f in zip(xs, xs[1:], scan_line) if f > 0)
        return area % (10**9 + 7)
