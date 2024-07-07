int main() {
    vector<int> arr;
    int k;
    cout << "Enter number of elements: ";
    cin >> k;
    for (int i = 0; i < k; i++) {
        cout << "Enter element " << i + 1 << ": ";
        int num;
        cin >> num;
        arr.push_back(num);
    }
    cout << "Sum of elements that are single-digit or two-digit numbers: " << add_elements(arr, k) << endl;
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