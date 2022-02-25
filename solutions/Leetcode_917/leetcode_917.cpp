#include <string>

class Solution1
{
public:
    std::string reverseOnlyLetters(std::string s)
    {
        size_t left = 0;
        size_t right = s.size() - 1;
        while (left < right)
        {
            if (!std::isalpha(s[left]))
                left++;
            else if (!std::isalpha(s[right]))
                right--;
            else
            {
                std::swap(s[left], s[right]);
                left++;
                right--;
            }
        }
        return s;
    }
};
