#include <sstream>
#include <string>

class Solution1
{
public:
    std::string complexNumberMultiply(std::string num1, std::string num2)
    {
        int plusIndex1 = num1.find('+');
        std::string real1 = num1.substr(0, plusIndex1), complex1 = num1.substr(plusIndex1 + 1, num1.size() - plusIndex1 - 2);
        int plusIndex2 = num2.find('+');
        std::string real2 = num2.substr(0, plusIndex2), complex2 = num2.substr(plusIndex2 + 1, num2.size() - plusIndex2 - 2);
        int real = std::stoi(real1) * std::stoi(real2) - std::stoi(complex1) * std::stoi(complex2);
        int complex = std::stoi(real1) * std::stoi(complex2) + std::stoi(real2) * std::stoi(complex1);
        return std::to_string(real) + "+" + std::to_string(complex) + "i";
    }
};

// Borrow from: https://leetcode.com/problems/complex-number-multiplication/discuss/100440/c%2B%2B-using-stringstream
class SolutionUsingStringStream
{
public:
    std::string complexNumberMultiply(std::string num1, std::string num2)
    {
        std::stringstream s1(num1), s2(num2), product;
        int real1, complex1, real2, complex2;
        char sign;
        s1 >> real1 >> sign >> complex1 >> sign;
        s2 >> real2 >> sign >> complex2 >> sign;
        product << (real1 * real2 - complex1 * complex2) << "+" << (real1 * complex2 + real2 * complex1) << "i";
        return product.str();
    }
};
