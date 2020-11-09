# https://leetcode.com/problems/string-to-integer-atoi/

import re

class Solution:
    def a_to_i(self, strs):
        num = re.findall(r'(^[\+\-0]*\d+)', strs.lstrip())
        print(num)
        if len(num) == 0:
            return 0
        elif int(num[0]) < -2**31:
            return -2**31
        elif int(num[0]) > 2**31 - 1:
            return 2**31 - 1
        else:
            return int(num[0])
        
if __name__ == "__main__":
    a = "  123abd"
    res = Solution().a_to_i(a)
    print(res)

    