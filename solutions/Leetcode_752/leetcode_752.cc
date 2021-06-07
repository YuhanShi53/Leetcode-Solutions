#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

class Solution {
public:
    int openLock(vector<string>& deadends, string target)
    {
        unordered_set<string> visited(deadends.begin(), deadends.end());
        if (visited.find("0000") != visited.end())
            return -1;
        queue<string> q;
        q.push("0000");
        int minimum_turn = -1;
        while (!q.empty())
        {
            int q_len = q.size();
            minimum_turn++;
            for (int i = 0; i < q_len; i++)
            {
                string num = q.front();
                q.pop();
                if (num == target)
                    return minimum_turn;
                if (visited.find(num) != visited.end())
                    continue;
                visited.insert(num);

                for (int i = 0; i < 4; i++)
                {
                    string tmp = num;
                    tmp[i] = (num[i] - '0' + 1) % 10 + '0';
                    q.push(tmp);
                    tmp[i] = (num[i] - '0' - 1 + 10) % 10 + '0';
                    q.push(tmp);
                }
            }
        }
        return -1;
    }
};