#include <set>

using namespace std;

class MyCalendar1
{
public:
    bool book(int start, int end)
    {
        auto itr = calendar.lower_bound({start, end});
        if ((itr == calendar.end() || itr->first >= end) && (itr == calendar.begin() || (--itr)->second <= start))
        {
            calendar.insert({start, end});
            return true;
        }
        return false;
    }

private:
    set<pair<int, int>> calendar;
};