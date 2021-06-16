#include <string>
#include <vector>

using namespace std;

class Solution1 {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> parenthesis;
        dfs(parenthesis, n, 0, "");
        return parenthesis;
    }

private:
    void dfs(vector<string> &parenthesis, int left, int right, string x)
    {
        if (left == 0 && right == 0)
            parenthesis.push_back(x);
        if (left)
            dfs(parenthesis, left - 1, right + 1, x + "(");
        if (right)
            dfs(parenthesis, left, right - 1, x + ")");
    }
};