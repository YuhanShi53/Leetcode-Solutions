#include <deque>
#include <vector>

class Solution1 {
public:
    std::vector<std::vector<int>> updateMatrix(std::vector<std::vector<int>>& mat) {
        int num_rows = mat.size();
        int num_cols = mat[0].size();
        int num_ones = num_rows * num_cols;
        std::deque<std::pair<int, int>> q;
        std::vector<std::vector<int>> ret(num_rows, std::vector<int>(num_cols, -1));
        int directions[5] = {1, 0, -1, 0, 1};

        for (int i = 0; i < num_rows; i++) {
            for (int j = 0; j < num_cols; j++) {
                if (mat[i][j] == 0) {
                    q.push_back(std::pair<int, int>(i, j));
                    ret[i][j] = 0;
                }
            }
        }

        int step = 1;
        while (num_ones) {
            int q_size = q.size();
            while (q_size) {
                int x = q.back().first;
                int y = q.back().second;
                q.pop_back();
                num_ones--;
                q_size--;
                for (int i = 0; i < 4; i++) {
                    int xx = x + directions[i];
                    int yy = y + directions[i+1];
                    if (0 <= xx && xx < num_rows && 0 <= yy && yy < num_cols && ret[xx][yy] < 0) {
                        ret[xx][yy] = step;
                        q.push_front({xx, yy});
                    }
                }
            }
            step++;
        }
        return ret;
    }
};