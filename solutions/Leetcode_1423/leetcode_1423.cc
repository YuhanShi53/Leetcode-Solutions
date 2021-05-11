#include <numeric>
#include <vector>

using namespace std;

class Solution1
{
public:
    int maxScore(vector<int> cardPoints, int k)
    {
        int length = cardPoints.size();
        if (k >= length)
            return accumulate(cardPoints.begin(), cardPoints.end(), 0);
        int score = accumulate(cardPoints.begin(), cardPoints.begin() + k, 0), max_score = score;
        for (int i = 1; i <= k; i++)
        {
            score = score - cardPoints[k - i] + cardPoints[length - i];
            max_score = max(score, max_score);
        }
        return max_score;
    }
};