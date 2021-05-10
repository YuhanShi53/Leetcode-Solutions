#include <math.h>
#include <numeric>
#include <vector>

using namespace std;

class Solution1
{
public:
    int countPrimes(int n)
    {
        if (n < 3)
            return 0;
        int n_sqrt = sqrt(n);
        vector<int> is_prime(n, 1);
        is_prime[0] = 0;
        is_prime[1] = 0;
        for (int x = 2; x <= n_sqrt; ++x)
        {
            if (is_prime[x])
            {
                for (int y = x; x * y < n; y++)
                    is_prime[x * y] = 0;
            }
        }
        return accumulate(is_prime.begin(), is_prime.end(), 0);
    }
};