#!/usr/local/env python
""" Leetcode 332 - Reconstruct Itinerary

https://leetcode.com/problems/reconstruct-itinerary/

1. self-implement: Time: 1016ms(5.07%) Memory: 15.4MB(5.07%)
2. DFS Recursive: Time: 80ms(81.77%) Memory: 14.1MB(71.11%)
3. DFS Iterative: Time: 76ms(92.69%) Memory: 14MB(89.14%)

"""

from collections import defaultdict
from copy import deepcopy
from typing import List

class Solution1:
    "self-implement"
    def find_itinerary(self, tickets: List[List[str]]) -> List[str]:
        from_to_dict = {}
        target_length = len(tickets) + 1
        for dep, des in tickets:
            from_to_dict[dep] = from_to_dict.get(dep, []) + [des]
        for value in from_to_dict.values():
            value.sort()
        return self.dfs('JFK', ['JFK'], target_length, from_to_dict)


    def dfs(self, s, current_list, target_length, from_to_dict):
        if len(current_list) == target_length:
            return current_list
        elif not from_to_dict.get(s, False) or len(from_to_dict[s]) == 0:
            return None
        
        for x in from_to_dict[s]:
            temp_dict = deepcopy(from_to_dict)
            temp_dict[s].remove(x)
            temp = self.dfs(x, current_list+[x], target_length, temp_dict)
            if temp is not None:
                return temp

        return None

class Solution2:
    """ DFS Recursive """
    def find_itinerary(self, tickets):
        tickets = sorted(tickets)[::-1]
        from_to = defaultdict(list)
        for dept, dest in tickets:
            from_to[dept] += [dest]
        itinerary = []

        def visit(dept):
            while(from_to[dept]):
                visit(from_to[dept].pop())
            itinerary.append(dept)

        visit('JFK')
        return itinerary[::-1]


class Solution3:
    """ DFS Iterative """
    def find_itinerary(self, tickets):
        tickets = sorted(tickets)[::-1]
        from_to = defaultdict(list)
        for dept, dest in tickets:
            from_to[dept] += [dest]
        
        stack = ['JFK']
        itinerary = []
        while stack:
            while from_to[stack[-1]]:
                stack.append(from_to[stack[-1]].pop())
            itinerary.append(stack.pop())
        return itinerary[::-1]

if __name__ == '__main__':
    tickets = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
    itinerary = Solution3().find_itinerary(tickets)
    print(itinerary)

