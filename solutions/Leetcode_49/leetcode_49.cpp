#include <algorithm>
#include <string>
#include <unordered_map>
#include <vector>

class Solution1
{
public:
    std::vector<std::vector<std::string>> groupAnagrams(std::vector<std::string>& strs)
    {
        std::unordered_map<std::string, std::vector<std::string>> anagramsMap;
        for (const std::string& word : strs)
        {
            std::string copyWord = word;
            std::sort(copyWord.begin(), copyWord.end());
            anagramsMap[copyWord].push_back(word);
        }
        std::vector<std::vector<std::string>> anagrams;
        for (const auto& keyAnagramPair : anagramsMap)
            anagrams.push_back(keyAnagramPair.second);
        return anagrams;
    }
};