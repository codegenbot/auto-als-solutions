bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

int main() {
    int b;
    vector<int> arr;
    cout << "Enter the numbers: ";
    for (int i = 0; i < 9; i++) {
        cin >> b;
        arr.push_back(b);
    }
    
    vector<string> result = by_length(arr);
    
    cout << "The numbers in descending order with their names are: ";
    for (string str : result) {
        cout << str << " ";
    }
    return 0;
}