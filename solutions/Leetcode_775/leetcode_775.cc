#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

class Solution1
{
public:
    bool isIdealPermutation(vector<int> &A)
    {
        for (int i = 0; i != A.size(); ++i)
            if (abs(A[i] - i) > 1)
                return false;
        return true;
    }
};

int main()
{
    vector<int> A{1, 0};
    bool ans = Solution1().isIdealPermutation(A);
    cout << ans << endl;
}