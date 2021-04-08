#include <string>
#include <iostream>

using namespace std;

class Solution1
{
public:
    bool halvesAreAlike(string s)
    {
        int half_len = s.size() / 2;
        int num_l = 0, num_r = 0;
        for (int i = 0; i < half_len; ++i)
        {
            s[i] = tolower(s[i]);
            s[i + half_len] = tolower(s[i + half_len]);
            if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u')
                ++num_l;
            if (s[i + half_len] == 'a' || s[i + half_len] == 'e' || s[i + half_len] == 'i' || s[i + half_len] == 'o' || s[i + half_len] == 'u')
                ++num_r;
        }
        return num_l == num_r;
    }
};

int main()
{
    string s{"textbook"};
    bool ans = Solution1().halvesAreAlike(s);
    cout << ans << endl;
}