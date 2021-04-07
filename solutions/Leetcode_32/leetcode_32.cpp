#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

class Solution1
{
public:
    int longestValidParentheses(string s)
    {
        stack<int> stk;
        int prev = 0, max_length = 0;
        for (auto x : s)
        {
            if (x == '(')
            {
                stk.push(prev);
                prev = 0;
            }
            else if (!stk.empty())
            {
                prev = prev + stk.top() + 2;
                max_length = max(max_length, prev);
                stk.pop();
            }
            else
            {
                prev = 0;
            }
        }
        return max_length;
    }
};

class Solution2
{
public:
    int longestValidParentheses(string s)
    {
        vector<int> dp(s.length() + 1, 0);
        int max_len = 0;
        for (int i = 1; i < s.length(); i++)
        {
            if (s[i] == ')')
            {
                if (s[i - 1] == '(')
                    dp[i] = (i - 2) >= 0 ? (dp[i - 2] + 2) : 2;
                else if (i - dp[i - 1] - 1 >= 0 && s[i - dp[i - 1] - 1] == '(')
                    dp[i] = dp[i - 1] + 2 + ((i - dp[i - 1] - 2 >= 0) ? dp[i - dp[i - 1] - 2] : 0);
                max_len = max(max_len, dp[i]);
            }
        }
        return max_len;
    }
};

int main()
{
    string s = "(()())";
    int ans = Solution2().longestValidParentheses(s);
    cout << ans << endl;
}