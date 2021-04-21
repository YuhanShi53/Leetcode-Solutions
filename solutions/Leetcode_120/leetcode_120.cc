#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Solution1
{
public:
    int minimumTotal(vector<vector<int>> &triangle)
    {
        vector<int> level = triangle[0];
        for (int i = 1; i != triangle.size(); ++i)
        {
            vector<int> temp = triangle[i];
            temp[0] += level[0];
            temp[temp.size() - 1] += level[level.size() - 1];
            for (int j = 1; j != temp.size() - 1; ++j)
                temp[j] += min(level[j - 1], level[j]);
            level = temp;
        }
        return *min_element(level.begin(), level.end());
    }
};

class Solution2
{
public:
    int minimumTotal(vector<vector<int>> &triangle)
    {
        vector<int> level = triangle.back();
        for (int i = triangle.size() - 2; i != -1; --i)
            for (int j = 0; j != triangle[i].size(); ++j)
                level[j] = triangle[i][j] + min(level[j], level[j + 1]);
        return level[0];
    }
};