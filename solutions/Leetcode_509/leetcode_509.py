class Solution1:
    def fib(self, n: int) -> int:
        return n if n < 2 else self.fib(n-1) + self.fib(n-2)


class Solution2:
    def fib(self, n):
        if n < 2:
            return n
        prev = [0, 1]
        while n >= 2:
            prev[0], prev[1] = prev[1], prev[0] + prev[1]
            n -= 1
        return prev[1]
