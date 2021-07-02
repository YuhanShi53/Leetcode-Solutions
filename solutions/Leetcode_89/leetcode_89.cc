#include <vector>

using namespace std;


class Solution1 {
public:
    vector<int> grayCode(int n) {
        vector<int> ret{0};
        for (int k = 0; k < n; ++k) {
            auto size_ret = ret.size();
            for (int i = size_ret-1; i >= 0; --i)
                ret.push_back(ret[i] ^ (1 << k));
        }
        return ret;
    }
};
