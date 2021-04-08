from typing import List


class Solution1:
    def letter_combinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = []

        def dfs(remain_digits, string):
            if remain_digits == '':
                combinations.append(string)
            else:
                for s in letters[int(remain_digits[0])-2]:
                    dfs(remain_digits[1:], string+s)

        dfs(digits, '')
        return combinations


class Solution2:
    def letter_combinations(self, digits):
        if digits == '':
            return []
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        combinations = ['']
        for i in range(len(digits)):
            temp = []
            while combinations:
                string = combinations.pop()
                for s in letters[int(digits[i]) - 2]:
                    temp.append(string + s)
            combinations = temp
        return combinations


if __name__ == '__main__':
    digits = '23'
    ans = Solution2().letter_combinations(digits)
    print(ans)
