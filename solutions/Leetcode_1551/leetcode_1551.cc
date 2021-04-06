/* Leetcode 1551 - Minimum Operations to Make Array Equal

https://leetcode.com/problems/minimum-operations-to-make-array-equal/

*/

class Solution1
{
public:
    int minOperations(int n)
    {
        return n * n >> 2;
    }
};
