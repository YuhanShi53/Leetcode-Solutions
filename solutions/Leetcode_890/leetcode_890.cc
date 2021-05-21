#include <string>
#include <unordered_map>
#include <vector>

using namespace std;


class Solution1
{
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern)
    {
        string p = normalize(pattern);
        vector<string> ret;
        for (string word : words)
        {
            string normalized_word = normalize(word);
            if (normalized_word == p)
                ret.push_back(word);
        }
        return ret;
    }

private:
    string normalize(string word)
    {
        unordered_map<char, int> mapping;
        for (int i = 0; i < word.size(); i++)
        {
            if (mapping.find(word[i]) == mapping.end())
                mapping[word[i]] = mapping.size();
            word[i] = 'a' + mapping[word[i]];
        }
        return word;
    }
};
