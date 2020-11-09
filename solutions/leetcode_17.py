# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombination(self, digits):

        if len(digits) == 0:
            return []

        self.look_up_dict = {"2": "abc",
                             "3": "def",
                             "4": "ghi",
                             "5": "jkl",
                             "6": "mno",
                             "7": "pqrs",
                             "8": "tuv",
                             "9": "wxyz"}

        res = []
        self.helper(digits, 0, "", res)
        return res

    def helper(self, digits, level, candidate, res):
        if level == len(digits):
            res.append(candidate)
            return

        for x in self.look_up_dict[digits[level]]:
            self.helper(digits, level+1, candidate + x, res)

if __name__ == "__main__":

    digits = "234"
    res = Solution().letterCombination(digits)
    print(res)