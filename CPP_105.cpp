bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

int main() {
    int b; // Declare variable b
    vector<int> arr = {1, 2, 3};
    vector<string> res = by_length(arr);
    
    cout << "Result: ";
    for (const string& str : res) {
        cout << str << " ";
    }
    cout << endl;
    
    return 0;
}