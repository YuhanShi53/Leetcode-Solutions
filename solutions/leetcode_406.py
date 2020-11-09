class Solution:
    def reconstruct_queue(self, people):
        self.sorted_queue = []
        people.sort(key=lambda x: x[0], reverse=True)
        self.bfs(people, [])
        return self.sorted_queue[::-1]

    def bfs(self, remained_people, sorted_queue):
        num_related_people = len(remained_people)
        for i, person in enumerate(remained_people):
            people_larger_and_before = person[1]
            if people_larger_and_before > i:
                return
            elif people_larger_and_before == i:
                if num_related_people > 1:
                    self.bfs(remained_people[0:i] + remained_people[i+1:], sorted_queue+[person])
                else:
                    self.sorted_queue = sorted_queue + [person]

if __name__ == "__main__":
    people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    res = Solution().reconstruct_queue(people)
    print(res)