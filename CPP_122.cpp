int main() {
    int arr[] = {1, 2, 3, 4, 5};
    vector<int> vec(arr, arr + sizeof(arr) / sizeof(arr[0]));
    int k = 3;
    assert(add_elements(vec, k) == 6);
    return 0;
}

int add_elements(vector<int> arr, int k) {
    int sum = 0;
    for (int i = 0; i < min(k, arr.size()); i++) {
        if (to_string(arr[i]).size() <= 2) {
            sum += arr[i];
        }
    }
    return sum;
}