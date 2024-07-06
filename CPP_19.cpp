string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
                                {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
                                {"eight", 8}, {"nine", 9}};
    string result = "";
    for (char c : numbers) {
        if (c == ' ') continue;
        result += numMap.begin()->first[numMap[c - '0']] + " ";
    }
    return result.substr(0, result.size() - 1);
}