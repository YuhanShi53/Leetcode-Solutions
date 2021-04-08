#include <string>
#include <vector>
#include <iostream>

using namespace std;

class Solution1
{
public:
    vector<string> letterCombination(string digits)
    {
        vector<string> combinations;
        if (digits.size() == 0)
            return combinations;
        string str;
        const vector<string> letters{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        dfs(str, digits, 0, combinations, letters);
        return combinations;
    }

    void dfs(string str, const string &digits, int id, vector<string> &combinations, const vector<string> &letters)
    {
        if (id == digits.size())
            combinations.push_back(str);
        else
        {
            for (auto s : letters[digits[id] - '0' - 2])
            {
                dfs(str + s, digits, id + 1, combinations, letters);
            }
        }
    }
};

class Solution2
{
public:
    vector<string> letterCombination(string digits)
    {
        vector<string> combinations;
        if (digits.size() == 0)
            return combinations;
        const vector<string> letters{"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
        combinations.push_back("");

        for (auto s : digits)
        {
            vector<string> temp;
            for (auto str : combinations)
            {
                for (auto x : letters[s - '0' - 2])
                    temp.push_back(str + x);
            }
            combinations.swap(temp);
        }
        return combinations;
    }
};