int add_elements(vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < min(k, arr.size()); i++) {
        if (to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;

}

int main() {
    assert(add_elements({1}, 1) == 1);
    // ... other test cases ...
    return 0;
}