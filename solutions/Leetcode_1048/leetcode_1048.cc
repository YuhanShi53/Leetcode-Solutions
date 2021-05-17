#include <algorithm>
#include <unordered_map>
#include <string>
#include <vector>

using namespace std;


class Solution1
{
public:
    static bool compare(const string &s1, const string &s2)
    {
        return s1.length() < s2.length();
    }

    int longestStrChain(vector<string>& words)
    {
        sort(words.begin(), words.end(), compare);
        unordered_map<string, int> chain_length;
        int max_len;
        for (string word : words)
        {
            for (int i = 0; i < word.length(); i++)
            {
                string prev = word.substr(0, i) + word.substr(i+1);
                chain_length[word] = max(chain_length[word], chain_length.find(prev) == chain_length.end() ? 1 : chain_length[prev] + 1);
            }
            max_len = max(max_len, chain_length[word]);
        }
        return max_len;
    }
};