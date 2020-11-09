# https://leetcode.com/problemset/all/?search=high%20five
# Time:100% Memory:100%

class Solution:
    def high_five(self, items):
        score_statistic = {}
        for item in items:
            student_id = item[0]
            student_score = item[1]
            if score_statistic.get(student_id, 0):
                score_statistic[student_id].append(student_score)
            else:
                score_statistic[student_id] = [student_score]

        high_five = []
        for student_id in score_statistic.keys():
            student_scores = score_statistic[student_id]
            student_scores.sort(reverse=True)
            high_five_average = sum(student_scores[0:5]) // 5
            high_five.append([student_id, high_five_average])

        return high_five

if __name__ == "__main__":
    items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    res = Solution().high_five(items)
    print(res)