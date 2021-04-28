class Solution1
{
public:
    int const IntMaxPowerThree = 1162261467;
    bool isPowerOfThree(int n)
    {
        return (n > 0) && (IntMaxPowerThree % n == 0);
    }
};