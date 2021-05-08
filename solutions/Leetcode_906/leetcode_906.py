import math


class Solution1:
    def super_palindromes_in_range(self, left: str, right: str) -> int:
        # Find low bound and high bound of substring to form palindrome
        left = int(left)
        right = int(right)
        sqrt_left = math.floor(math.sqrt(left))
        sqrt_right = math.ceil(math.sqrt(right))
        len_low = math.ceil(len(str(sqrt_left)) / 2)
        len_high = math.ceil(len(str(sqrt_right)) / 2)
        low = 10 ** (len_low-1)
        high = 10 ** len_high
        # Generate palindrome and add count if sqaure is palindrome
        count = 0
        for x in range(low, high):
            x = str(x)
            for num in (x+x[::-1], x[:-1]+x[::-1]):
                num = int(num)**2
                if left <= num <= right and str(num) == str(num)[::-1]:
                    count += 1
        return count


if __name__ == '__main__':
    left = '1'
    right = '2'
    ans = Solution1().super_palindromes_in_range(left, right)
    print(ans)
