int main() {
    vector<int> arr;
    int k;

    cout << "Enter number of elements: ";
    cin >> k;

    cout << "Enter the elements: ";
    for (int i = 0; i < k; i++) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    int sum = add_elements(arr, k);

    cout << "The sum of all numbers that are single-digit or two-digit is: " << sum << endl;

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