#include <functional>
#include <stack>
#include <string>
#include <unordered_map>
#include <vector>


using namespace std;


class Solution1
{
public:
    int evalRPN(vector<string> &tokens)
    {
        unordered_map<string, function<int (int, int)>> mapping = {
            {"+", [](int a, int b){return a + b;}},
            {"-", [](int a, int b){return a - b;}},
            {"*", [](int a, int b){return a * b;}},
            {"/", [](int a, int b){return a / b;}},
        };

        stack<int> numbers;
        for (auto token : tokens)
        {
            if (!mapping.count(token))
            {
                numbers.push(stoi(token));
            } else {
                int right = numbers.top();
                numbers.pop();
                int left = numbers.top();
                numbers.pop();
                numbers.push(mapping[token](left, right));
            }
        }
        return numbers.top();
    }
};