class Solution1:
    def remove_duplicates(self, S: str) -> str:
        stack = []
        for x in S:
            if stack and stack[-1] == x:
                stack.pop()
            else:
                stack.append(x)
        return "".join(stack)
