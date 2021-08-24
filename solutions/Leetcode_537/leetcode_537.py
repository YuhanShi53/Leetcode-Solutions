class Solution1:
    def complex_number_multiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        real1, complex1 = int(num1[0]), int(num1[1][:-1])
        real2, complex2 = int(num2[0]), int(num2[1][:-1])
        real = real1 * real2 - complex1 * complex2
        complex = real1 * complex2 + real2 * complex1
        return '%d+%di' % (real, complex)
