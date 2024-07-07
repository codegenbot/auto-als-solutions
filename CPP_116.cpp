Here is the solution:

vector<int> sort_array(vector<int> arr) {
    stable_partition(arr.begin(), arr.end(),
        [](int x) { return __builtin_popcount(x); });
    return arr;
}