#include <iostream>
#include <vector>

int max_fill(std::vector<std::vector<int>> grid, int capacity) {
    int total_water = 0;
    for (const auto& row : grid) {
        for (int amount : row) {
            total_water += amount;
        }
    }

    return total_water / capacity + ((total_water % capacity) != 0);
}

int main() {
    std::vector<std::vector<int>> grid = {{1,1,1,1}, {1,1,1,1}};
    int capacity = 9;
    std::cout << max_fill(grid, capacity) << std::endl;
    return 0;
}