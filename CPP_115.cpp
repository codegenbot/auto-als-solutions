int main() {
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
    };

    std::vector<std::vector<int>> grid = {{1,1,1,1}, {1,1,1,1}};
    int capacity = 9;

    int result = max_fill(grid, capacity);

    std::cout << "The maximum fill is: " << result << std::endl;
    
    return 0;
}