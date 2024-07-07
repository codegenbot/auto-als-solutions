#include <vector>

int max_fill(vector<vector<int>> grid, int capacity) {
    int total_water = 0;
    for (const auto& row : grid) {
        for (int water : row) {
            if (water == 1) {
                total_water += 1; // assuming you want to count each cell as 1 unit of water
            }
        }
    }

    return (total_water + capacity - 1) / capacity;
}