# https://leetcode.com/problems/divide-two-integers/

class Solution:
    def divide(self, dividend, divisor):
        INT_MAX = 2**31-1
        INT_MIN = -2**31
        if dividend == INT_MIN and abs(divisor) == 1:
            return INT_MAX if divisor == -1 else INT_MIN

        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)

        if(abs_dividend < abs_divisor):
            return 0

        res = self._unsigned_divide(abs_dividend, abs_divisor)
        return -res if ((dividend < 0) ^ (divisor < 0)) else res

    def _unsigned_divide(self, dividend, divisor):
        dividend = abs(dividend)
        divisor = abs(divisor)
        count = 0
        while(dividend >= divisor):
            local_count = 1
            copy_of_divisor = divisor
            while(dividend > (copy_of_divisor << 1)):
                copy_of_divisor <<= 1
                local_count <<= 1
            count += local_count
            dividend -= copy_of_divisor
        return count

if __name__ == "__main__":
    dividend = 4
    divisor = 2
    res = Solution().divide(dividend, divisor)
    print(res)
