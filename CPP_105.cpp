bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

int main() {
    int b;
    vector<int> arr = {1, 2, 3, 4, 5};
    vector<string> result = by_length(arr);
    if (issame(result, {"One", "Two", "Three", "Four", "Five"})) {
        cout << "The vectors are the same";
    } else {
        cout << "The vectors are not the same";
    }
    return 0;
}