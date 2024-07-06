```cpp
int max_fill(vector<vector<int>> grid, int capacity) {
    int total_water = 0;
    for (const auto& row : grid) {
        total_water += accumulate(row.begin(), row.end(), 0);
    }
    
    int times_to_lower_buckets = -(-total_water / capacity); // integer division
    
    return times_to_lower_buckets;
}