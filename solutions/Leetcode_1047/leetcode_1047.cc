#include <stack>
#include <string>

using namespace std;

class Solution1 {
public:
    string removeDuplicates(string s) {
        string ret = "";
        for (char& x : s) {
            if (!ret.empty() && ret.back() == x)
                ret.pop_back();
            else
                ret.push_back(x);
        }
        return ret;
    }
};
