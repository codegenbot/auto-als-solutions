int main() {
    vector<int> arr;
    int k;

    cout << "Enter array elements (space separated): ";
    cin >> ws;
    for (string s; getline(cin, s);) {
        arr.push_back(stoi(s));
    }

    cout << "Enter the value of k: ";
    cin >> k;

    int result = add_elements(arr, k);
    cout << "Sum of elements less than or equal to 2 digits: " << result << endl;
    
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