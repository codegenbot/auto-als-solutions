Here is the solution:

vector<vector<int>> get_row(vector<vector<int>> lst, int x) {
    vector<pair<int, int>> result;
    for (int i = 0; i < lst.size(); i++) {
        if (i == x) {
            for (int j = lst[i].size() - 1; j >= 0; j--) {
                result.push_back({i, j});
            }
        }
    }
    return vector<vector<int>>(result.begin(), result.end());
}