bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

int main() {
    int b; // Declare variable 'b'
    
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<string> result = by_length(arr);
    
    if (issame(by_length({1, 2, 3}), result)) {
        cout << "The vectors are the same";
    } else {
        cout << "The vectors are not the same";
    }
    
    return 0;
}