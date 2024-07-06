#include <iostream>
#include <vector>
#include <cmath>
#include <random>

bool issame(vector<int> a,vector<int>b){
    if(a.size() != b.size())
        return false;
    for(int i = 0; i < a.size(); i++)
        if(a[i] != b[i])
            return false;
    return true;
}

vector<vector<int>> minPath(vector<vector<int>>& grid, int k) {
    vector<int> result;
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
            int dx = gen() % 4;
            int nx = x + directions[dx][0], ny = y + directions[dx][1];
            if (nx >= 0 && nx < grid.size() && ny >= 0 && ny < grid.size()) {
                for (int i = 0; i < grid.size(); ++i) {
                    if (grid[i][ny] == result.size())
                        x = i, y = ny;
                }
            }
        }
        result.push_back(grid[x][y]);
    }
    return result;
}

int main() {
    assert(issame(minPath({{1, 3}, {3, 2}}, 10), vector<int>({1, 3, 1, 3, 1, 3, 1, 3, 1, 3})));
    return 0;
}