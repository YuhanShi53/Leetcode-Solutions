from typing import List


class Solution1:
    def maximum_units(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units = 0
        for num, unit in boxTypes:
            n = num if truckSize >= num else truckSize
            truckSize -= n
            units += n * unit
            if truckSize == 0:
                return units
        return units
