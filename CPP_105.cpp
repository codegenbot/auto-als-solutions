Here is the completed code:

vector<string> by_length(vector<int> arr) {
    vector<int> numbers;
    for (int i : arr) {
        if (i >= 1 && i <= 9)
            numbers.push_back(i);
    }
    sort(numbers.begin(), numbers.end());
    reverse(numbers.begin(), numbers.end());
    vector<string> result;
    for (int num : numbers) {
        result.push_back(to_string(num) == "1" ? "One"
                          : to_string(num) == "2" ? "Two"
                          : to_string(num) == "3" ? "Three"
                          : to_string(num) == "4" ? "Four"
                          : to_string(num) == "5" ? "Five"
                          : to_string(num) == "6" ? "Six"
                          : to_string(num) == "7" ? "Seven"
                          : to_string(num) == "8" ? "Eight"
                          : to_string(num) == "9" ? "Nine"
                          : "");
    }
    return result;
}