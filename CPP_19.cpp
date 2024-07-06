string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    vector<string> nums;
    string num;

    // split the input string into individual numbers
    for (int i = 0; i < numbers.length(); i++) {
        while (i + 1 <= numbers.length() && !ispunct(numbers[i])) {
            i++;
        }
        num += numbers.substr(i - (numbers[i] == ' ') ? 0 : i - 1, 4);
    }

    // sort the numbers based on their integer value
    sort(nums.begin(), nums.end(), [&numMap](string a, string b) {
        return to_string(numMap[a]) > to_string(numMap[b]);
    });

    // join the sorted numbers into a single string
    return join(nums, " ");
}

string join(vector<string>& vec, string sep) {
    string result = "";
    for (int i = 0; i < vec.size(); ++i) {
        result += vec[i];
        if (i != vec.size() - 1)
            result += sep;
    }
    return result;
}