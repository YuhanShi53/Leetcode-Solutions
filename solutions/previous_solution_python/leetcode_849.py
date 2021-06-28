# https://leetcode.com/problems/maximize-distance-to-closest-person/submissions/
# Time:10.78% Memory:79.17%

class Solution():
    def maximize_dist_to_cloest(self, seats):
        non_empty_seats = []
        for idx, seat in enumerate(seats):
            if seat == 1:
                non_empty_seats.append(idx)
        
        pointer = 0
        left_cloest = non_empty_seats[pointer]
        right_cloest = non_empty_seats[pointer]
        non_empty_count = len(non_empty_seats) - 1
        max_distance = 0

        for idx, seat in enumerate(seats):
            if idx >= right_cloest and left_cloest < non_empty_seats[-1]:
                pointer += 1
                left_cloest = right_cloest
                right_cloest = non_empty_seats[min(pointer, non_empty_count)]
            
            if seat == 0:
                distance_to_cloest = min(abs(left_cloest-idx), \
                    abs(right_cloest-idx))
                max_distance = max(distance_to_cloest, max_distance)

        return max_distance

if __name__ == "__main__":
    seats = [0,0,1,1,1,0,0,0,0,1,0,0,0,0,0,0]
    max_distance = Solution().maximize_dist_to_cloest(seats)
    print(max_distance)