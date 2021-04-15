class Solution1
{
public:
    int fib(int n)
    {
        if (n < 2)
            return n;
        return fib(n - 1) + fib(n - 2);
    }
};

class Solution2
{
public:
    int fib(int n)
    {
        if (n < 2)
            return n;
        int a = 0, b = 1, temp = 0;
        while (n >= 2)
        {
            temp = a + b;
            a = b;
            b = temp;
            n--;
        }
        return b;
    }
};