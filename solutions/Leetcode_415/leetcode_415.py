class Solution1:
    def add_string(self, num1: str, num2: str) -> str:
        ret = []
        add_one = 0
        if len(num1) > len(num2):
            num2 = '0' * (len(num1)-len(num2)) + num2
        elif len(num1) < len(num2):
            num1 = '0' * (len(num2)-len(num1)) + num1
        for i in range(len(num1)-1, -1, -1):
            x = (ord(num1[i])-48) + (ord(num2[i])-48) + add_one
            add_one = x // 10
            x = str(x % 10)
            ret.append(x)
        if add_one:
            ret.append('1')
        return ''.join(ret[::-1])
