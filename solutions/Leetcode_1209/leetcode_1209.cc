#include <iosteam>
#include <string>
#include <vector>

using namespace std;

class Solution1
{
public:
    string removeDuplicates(string s, int k)
    {
        vector<pair<char, int>> stk;
        for (auto x : s)
        {
            if (stk.empty() || stk.back().first != x)
            {
                stk.push_back({x, 1});
            }
            else if (stk.back().second + 1 == k)
            {
                stk.pop_back();
            }
            else
            {
                ++stk.back().second;
            }
        }
        string ans;
        for (auto p : stk)
            ans.append(p.second, p.first);
        return ans;
    }
};

int main()
{
    string s = "abcd";
    int k = 3;
    string ans = Solution1().removeDuplicates(s, k);
    cout << ans << endl;
    return 0;
}