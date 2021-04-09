#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

using namespace std;

class Solution1
{
public:
    bool isAlienSorted(vector<string> &words, string order)
    {
        int mapping[26];
        for (int i = 0; i < 26; i++)
            mapping[order[i] - 'a'] = i;
        for (int k = 1; k < words.size(); k++)
        {
            for (int j = 0; j < words[k - 1].length(); j++)
            {
                if (j == words[k].length() || mapping[words[k - 1][j] - 'a'] > mapping[words[k][j] - 'a'])
                    return false;
                if (mapping[words[k - 1][j] - 'a'] < mapping[words[k][j] - 'a'])
                    break;
            }
        }
        return true;
    }
};

class Solution2
{
    // Simplified of Solution1
    // Borrow from: https://leetcode.com/problems/verifying-an-alien-dictionary/discuss/203185/JavaC%2B%2BPython-Mapping-to-Normal-Order
public:
    bool isAlienSorted(vector<string> &words, string order)
    {
        int mapping[26];
        for (int i = 0; i < 26; i++)
            mapping[order[i] - 'a'] = i;
        for (auto &word : words)
            for (auto &c : word)
                c = mapping[c - 'a'];
        return is_sorted(words.begin(), words.end());
    }
};

int main()
{
    vector<string> word{"hello", "leetcode"};
    string order{"hlabcdefgijkmnopqrstuvwxyz"};
    bool ans = Solution1().isAlienSorted(word, order);
    cout << ans << endl;
}