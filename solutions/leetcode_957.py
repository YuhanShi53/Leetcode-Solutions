class Solution1:
    def prison_after_days(self, cells, N):
        temp = [0 for i in range(len(cells))]
        num_to_count = {}
        count_to_num = {}
        count = 0
        num = self.cells_to_num(cells)
        num_to_count[num] = count
        count_to_num[count] = num

        while count < N:
            num = 0
            for j in range(1, len(cells)-1):
                if cells[j-1] == cells[j+1]:
                    temp[j] = 1
                else:
                    temp[j] = 0
                num += temp[j] * 2**(7-j)
            cells = temp.copy()
            count += 1

            if num_to_count.get(num, 0):
                first_count = num_to_count[num]
                idx = (N - count + 1) % (count - first_count)
                if idx == 0:
                    return self.num_to_cells(count_to_num[count - 1])
                return self.num_to_cells(count_to_num[first_count+idx-1])
            else:
                num_to_count[num] = count
                count_to_num[count] = num
        return cells

    def num_to_cells(self, num):
        temp = [0 for i in range(8)]
        for i in range(8):
            if num >= 2**(7-i):
                num -= 2**(7-i)
                temp[i] = 1
        return temp

    def cells_to_num(self, cells):
        num = 0
        for i in range(len(cells)):
            num += cells[i] * 2**(7-i)
        return num

        

if __name__ == '__main__':
    cells = [1,0,0,1,0,0,1,0]
    N = 1000000000
    res = Solution1().prison_after_days(cells, N)
    print(res)