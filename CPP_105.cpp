```cpp
bool issame(vector<string> a, vector<string>b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

vector<string> by_length(vector<int> arr) {
    vector<string> numbers;
    for (int num : arr) {
        if (num >= 1 && num <= 9) {
            numbers.push_back(num > 5 ? "Greater than five" : to_string(num));
        }
    }
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
    vector<string> result;
    map<int, string> numberNames = {{1, "One"}, {2, "Two"}, {3, "Three"},
                                     {4, "Four"}, {5, "Five"}, {6, "Six"},
                                     {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    for (int num : numbers) {
        result.push_back(numberNames[num] != "" ? numberNames[num] : "Less than or equal to five");
    }
    return result;
}

int main() {
    assert(by_length({9, 4, 8}) == vector<string>{"Nine", "Eight", "Four"});
    return 0;
}