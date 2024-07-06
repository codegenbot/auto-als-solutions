int max_fill(vector<vector<int>> grid, int capacity) {
    int total_water = 0;
    for (const auto &row : grid) {
        for (int water : row) {
            total_water += water;
        }
    }

    int times_to_lower_bucket = total_water / capacity;

    if (total_water % capacity != 0) {
        times_to_lower_bucket++;
    }

    return times_to_lower_bucket;
}