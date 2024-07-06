int max_fill(vector<vector<int>> grid, int capacity) {
    int ans = 0, tot_water = 0;
    for (vector<int> row : grid) {
        tot_water += accumulate(row.begin(), row.end(), 0);
    }
    while (tot_water > 0) {
        int water_taken = min(tot_water, capacity);
        tot_water -= water_taken;
        ans++;
    }
    return ans;
}