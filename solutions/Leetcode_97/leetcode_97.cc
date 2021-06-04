#include <string>
#include <vector>

using namespace std;


class Solution1
{
public:
    bool isInterleave(string s1, string s2, string s3)
    {
        if (s1.length() + s2.length() != s3.length())
            return false;
        vector<vector<bool>> invalid(s1.length()+1, vector<bool>(s2.length()+1, false));
        return compare(s1, s2, s3, 0, 0, 0, invalid);
    }

private:
    bool compare(string &s1, string &s2, string &s3, int i, int j, int k, vector<vector<bool>> &invalid)
    {
        if (invalid[i][j])
            return false;
        if (k == s3.length())
            return true;
        bool is_valid = i < s1.length() && s1[i] == s3[k] && compare(s1, s2, s3, i+1, j, k+1, invalid) ||
            j < s2.length() && s2[j] == s3[k] && compare(s1, s2, s3, i, j+1, k+1, invalid);
        if (!is_valid)
            invalid[i][j] = true;
        return is_valid;
    }
};


class Solution2
{
public:
    bool isInterleave(string s1, string s2, string s3)
    {
        int s1_len = s1.size(), s2_len = s2.size(), s3_len = s3.size();
        if (s1_len + s2_len != s3_len)
            return false;
        bool invalid[s2_len+1];
        invalid[0] = true;
        for (int i = 1; i < s2_len+1; i++)
            invalid[i] = invalid[i-1] && s2[i-1] == s3[i-1];
        for (int i = 1; i < s1_len+1; i++)
        {
            invalid[0] = invalid[0] && s1[i-1] == s3[i-1];
            for (int j = 1; j < s2_len+1; j++)
                invalid[j] = (invalid[j-1] && s2[j-1] == s3[i+j-1]) || (invalid[j] && s1[i-1] == s3[i+j-1]);
        }
        return invalid[s2_len];
    }
};