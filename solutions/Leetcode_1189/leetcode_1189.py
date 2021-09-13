from collections import Counter


class Solution1:
    def max_number_of_balloons(self, text: str) -> int:
        counter = Counter(text)
        return min(counter['b'], counter['a'], counter['l']//2, counter['o']//2, counter['n'])


class SolutionMINE:
    def max_number_of_balloons(self, text: str) -> int:
        balloon = {'b': 0, 'a': 1, 'l': 2, 'o': 3, 'n': 4}
        balloon_count = [1, 1, 2, 2, 1]
        text_count = [0, 0, 0, 0, 0]
        for x in text:
            if x in balloon.keys():
                text_count[balloon[x]] += 1
        count = 0
        while True:
            for i in range(5):
                text_count[i] -= balloon_count[i]
                if text_count[i] < 0:
                    return count
            count += 1
