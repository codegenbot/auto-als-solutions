Here is the completed code:

int max_fill(vector<vector<int>> grid, int capacity) {
    int ans = 0;
    for (const auto &row : grid) {
        int remaining_water = 0;
        for (int water : row) {
            remaining_water += water;
            if (remaining_water > capacity) {
                while (remaining_water > 0) {
                    remaining_water -= capacity;
                    ans++;
                }
            }
        }
    }
    return ans;
}