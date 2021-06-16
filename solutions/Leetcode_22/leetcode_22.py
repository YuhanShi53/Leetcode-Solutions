from typing import List


class SolutionMINE:
    def generate_parenthesis(self, n: int) -> List[str]:
        parenthesis = []

        def dfs(left, right, x):
            if left == right == 0:
                parenthesis.append(x)
            if left:
                dfs(left-1, right+1, x + '(')
            if right:
                dfs(left, right-1, x + ')')
        dfs(n, 0, '')
        return parenthesis
