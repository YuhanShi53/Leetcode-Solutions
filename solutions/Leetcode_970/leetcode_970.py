class Solution1:
    def powerful_integers(self, x, y, bound):
        s = set()
        i = 1
        while i <= bound:
            j = 1
            while i + j <= bound:
                s.add(i+j)
                if y == 1:
                    break
                j *= y
            if x == 1:
                break
            i *= x
        return list(s)


class SolutionPythonicOf1:
    def powerful_integers(self, x, y, bound):
        power_x = {x**i for i in range(20) if x**i <= bound}
        power_y = {y**j for j in range(20) if y**j <= bound}
        return list({xx + yy for xx in power_x for yy in power_y if xx+yy <= bound})
