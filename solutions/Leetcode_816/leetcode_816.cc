#include <string>
#include <vector>

using namespace std;

class Solution1
{
public:
    vector<string> ambiguousCoordinates(string s)
    {
        int n = s.size();
        vector<string> ans;
        for (int length = 1; length < n - 2; length++)
        {
            vector<string> leftCandidates = getCandidates(s.substr(1, length));
            vector<string> rightCandidates = getCandidates(s.substr(1 + length, n - 2 - length));
            for (string left : leftCandidates)
                for (string right : rightCandidates)
                    ans.push_back("(" + left + ", " + right + ")");
        }
        return ans;
    }

    vector<string> getCandidates(string s)
    {
        int n = s.size();
        if (n == 1)
            return {s};
        if (*s.begin() == '0' && *(s.end() - 1) == '0')
            return {};
        if (*s.begin() == '0')
            return {"0." + s.substr(1)};
        if (*(s.end() - 1) == '0')
            return {s};
        vector<string> res{s};
        for (int i = 1; i < n; i++)
            res.push_back(s.substr(0, i) + '.' + s.substr(i));
        return res;
    }
};