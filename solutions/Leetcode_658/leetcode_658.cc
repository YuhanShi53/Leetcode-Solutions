#include <cmath>
#include <deque>
#include <vector>

using namespace std;


class Solution1 {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        int left = 0, right = arr.size() - k;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (x - arr[mid] > arr[mid+k] - x)
                left = mid + 1;
            else
                right = mid;
        }
        return vector<int>(arr.begin() + left, arr.begin() + left + k);
    }
};


class Solution2 {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        deque<int> ret;
        for (int& y : arr) {
            if (ret.size() < k)
                ret.push_back(y);
            else if (abs(x - y) < abs(x - ret.front())) {
                ret.pop_front();
                ret.push_back(y);
            }
        }
        return vector<int>(ret.begin(), ret.end());
    }
};