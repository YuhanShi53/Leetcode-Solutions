from bisect import bisect_left


class MyCalendar1:

    def __init__(self):
        self._calendar = []

    def book(self, start: int, end: int) -> bool:
        idx = bisect_left(self._calendar, (start, end))
        if ((idx == 0 or self._calendar[idx-1][1] <= start)
                and (idx == len(self._calendar) or self._calendar[idx][0] >= end)):
            self._calendar.insert(idx, (start, end))
            return True
        return False
