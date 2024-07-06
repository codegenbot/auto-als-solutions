#include <vector>
#include <cmath>
#include <random>

bool issame(int a, int b) { return abs(a - b) == 1; }

std::vector<int> minPath(const std::vector<std::vector<int>>& grid, int k) {
    std::vector<int> result;
    for (int i = 0; i < pow(grid.size(), 2); ++i) {
        bool found = false;
        for (int j = 0; j < grid.size(); ++j) {
            for (int l = 0; l < grid.size(); ++l) {
                if (grid[j][l] == i + 1) {
                    int x = j, y = l;
                    found = true;
                    break;
                }
            }
            if (found)
                break;
        }
        for (int t = 0; t < k; ++t) {
            std::vector<int> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
            std::random_device rd;
            std::mt19937 gen(rd());
            std::uniform_int_distribution<> dis(0, 3);
            int dx = dis(gen);
            int nx = x + directions[dx][0], ny = y + directions[dx][1];
            if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid.size()) {
                for (int i = 0; i < grid.size(); ++i) {
                    if (grid[i][ny] == result.size())
                        x = i, y = ny;
                }
            }
        }
        int val = grid[x][y];
        while (!issame(val, i + 1)) {
            for (int t = 0; t < k; ++t) {
                dx = dis(gen);
                nx = x + directions[dx][0], ny = y + directions[dx][1];
                if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid.size()) {
                    val = grid[nx][ny];
                    x = nx, y = ny;
                }
            }
        }
        result.push_back(val);
    }
    return result;
}