import math


class Solution1:
    def count_primes


class SolutionMINE:
    def count_primes(self, n: int) -> int:
        if n < 3:
            return 0
        sqrt_n = math.floor(math.sqrt(n))
        is_prime = [0, 0] + [1 for _ in range(n-2)]
        for x in range(2, sqrt_n+1):
            if is_prime[x]:
                is_prime[x*x:n:x] = [0] * len(is_prime[x*x:n:x])
        return sum(is_prime)


if __name__ == '__main__':
    n = 2
    ans = SolutionMINE().count_primes(n)
    print(ans)
