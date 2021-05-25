from typing import List


class Solution1:
    def eval_RPN(self, tokens: List[str]) -> int:
        numbers = []
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                num2 = numbers.pop()
                num1 = numbers.pop()
                if token == '+':
                    numbers.append(num1 + num2)
                elif token == '-':
                    numbers.append(num1 - num2)
                elif token == '*':
                    numbers.append(num1 * num2)
                else:
                    numbers.append(int(num1 / num2))
            else:
                numbers.append(int(token))
        return numbers.pop()


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11",
              "*", "/", "*", "17", "+", "5", "+"]
    ans = Solution1().eval_RPN(tokens)
    print(ans)
