from time import time

class Solution:
    def combination_sum(self, candidates, target):
        if min(candidates) > target:
            return []
        elif min(candidates) == target:
            return [[target]]

        self.target = target
        self.combinations = []
        candidates.sort()
        self.__dfs([], 0, candidates)
        return self.combinations

    def __dfs(self, last_combination, last_sum, last_candidates):
        for i, candidate in enumerate(last_candidates):
            current_sum = last_sum + candidate
            current_combination = last_combination + [candidate]
            rest_candidates = last_candidates[i+1:]
            if current_sum > self.target:
                return
            elif i > 0 and candidate == last_candidates[i-1]:
                continue
            elif current_sum == self.target:
                self.combinations.append(current_combination)
            elif current_sum < self.target:
                self.__dfs(current_combination, current_sum, rest_candidates)

if __name__ == "__main__":
    candidates = [10,1,2,7,6,1,5]
    target = 8
    start_time = time()
    res = Solution().combination_sum(candidates, target)
    end_time = time()
    print(res)
    print("Function time: %f" % (end_time-start_time))