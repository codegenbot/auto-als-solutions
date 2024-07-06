vector<int> maximum(vector<int> arr, int k) {
    vector<int> result(arr.size());
    for (int i = 0; i < arr.size(); i++) {
        result[i] = arr[i];
    }
    sort(result.begin(), result.end());
    for (int i = result.size() - 1; i >= result.size() - k; i--) {
        return {result[i]};
    }
}