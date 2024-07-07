vector<pair<int, int>> pluck(vector<int> arr) {
    vector<pair<int, int>> result;
    if (arr.empty()) return vector<pair<int, int>>({});

    pair<int, int> smallest = {INT_MAX, -1};
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] % 2 == 0 && arr[i] < smallest.first) {
            smallest = {{arr[i], i}};
        } else if (arr[i] % 2 == 0 && arr[i] == smallest.first) {
            smallest = {{arr[i], i}};
        }
    }

    return vector<pair<int, int>>({smallest});
}