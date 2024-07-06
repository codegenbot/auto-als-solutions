#include <iostream>
#include <vector>
#include <numeric>

int main() {
    int max_fill(std::vector<std::vector<int>> grid, int capacity) {
        int total_water = 0;
        for (const auto& row : grid) {
            total_water += std::accumulate(row.begin(), row.end(), 0);
        }
        
        int buckets_needed = total_water / capacity;
        if (total_water % capacity != 0)
            ++buckets_needed;

        return buckets_needed;
    }

    std::vector<std::vector<int>> grid = {{1,1,1,1}, {1,1,1,1}};
    int capacity = 9;
    int result = max_fill(grid, capacity);
    std::cout << "The minimum number of buckets needed is: " << result << std::endl;

    return 0;
}