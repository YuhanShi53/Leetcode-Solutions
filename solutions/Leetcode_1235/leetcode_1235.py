from typing import List


class SolutionMINE:
    def job_scheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        profit_list = []
        schedule = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])
        for start, end, profit in schedule:
            max_profit_idx = len(profit_list) - 1
            while max_profit_idx >= 0 and start < profit_list[max_profit_idx][1]:
                max_profit_idx -= 1
            current_profit = profit + (profit_list[max_profit_idx][0] if max_profit_idx >= 0 else 0)
            insert_position = self._binary_search(profit_list, current_profit)
            profit_list.insert(insert_position, (current_profit, end))
        return profit_list[-1][0]

    def _binary_search(self, profit_list, target) -> int:
        left = 0
        right = len(profit_list)
        while left < right:
            mid = left + (right - left) // 2
            if profit_list[mid][0] >= target:
                right = mid
            else:
                left = mid + 1
        return left
