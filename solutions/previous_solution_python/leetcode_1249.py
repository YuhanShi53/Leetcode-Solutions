""" Leetcode 1249 - Minimum Remove to Make Valid Parenthese

https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

1. Time: O(n) Memory: O(n) (n is length of string)
2. Time: O(n) Memory: O(n) (n is length of string)

"""


class Solution1:
    """ 1. MINE | Two-Pass """

    def min_remove_to_make_valid(self, s: str) -> str:
        rest, num_left_paren = [], 0
        for x in s:
            if x.isalpha():
                rest.append(x)
            elif x == '(':
                rest.append(x)
                num_left_paren += 1
            elif num_left_paren:
                rest.append(x)
                num_left_paren -= 1
        res, num_right_paren = [], 0
        for x in rest[::-1]:
            if x.isalpha():
                res.append(x)
            elif x == ')':
                res.append(x)
                num_right_paren += 1
            elif num_right_paren:
                res.append(x)
                num_right_paren -= 1
        return ''.join(res[::-1])


class Solution2:
    """ 2. Simiplified of 1 """

    def min_remove_to_make_valid(self, s):
        res, count = list(s), 0
        for i, x in enumerate(res):
            if x == '(':
                count += 1
            elif x == ')':
                if count:
                    count -= 1
                else:
                    res[i] = ''
        i = len(res) - 1
        while count:
            if res[i] == '(':
                res[i] = ''
                count -= 1
            i -= 1
        return ''.join(res)


if __name__ == '__main__':
    s = '))(('
    res = Solution1().min_remove_to_make_valid(s)
    print(res)
