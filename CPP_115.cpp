int main() {
    int rows = 2;
    int cols = 4;
    std::vector<std::vector<int>> grid(rows, std::vector<int>(cols));
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if ((i == 0 && j % 2 != 0) || (i == 1 && j % 2 == 0)) {
                grid[i][j] = 1;
            } else {
                grid[i][j] = 0;
            }
        }
    }

    int capacity = 9;
    int result = max_fill(grid, capacity);
    std::cout << "The maximum number of times the bucket can be filled is: " << result << std::endl;

    return 0;
}

int max_fill(std::vector<std::vector<int>> grid, int capacity) {
    int rows = grid.size();
    int cols = grid[0].size();
    int total_water = 0;
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (grid[i][j] == 1) {
                total_water++;
            }
        }
    }

    int max_lowerings = total_water / capacity;
    return max_lowerings + (total_water % capacity > 0);
}