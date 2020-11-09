# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def int_to_roman(self, nums):

        if nums is None or nums == 0:
            return ""
        
        look_up_dict = {5: "V",
                        10: "X",
                        50: "L",
                        100: "C",
                        500: "D",
                        1000: "M"}

        