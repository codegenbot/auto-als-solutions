string int_to_mini_roman(int number) {
    vector<pair<int, string>> romanNums = {{1000, "m"}, {900, "cm"}, {500, "d"},
                                            {400, "cd"}, {100, "c"}, {90, "cx"},
                                            {50, "l"}, {40, "xl"}, {10, "x"},
                                            {9, "ix"}, {5, "v"}, {4, "iv"},
                                            {1, "i"}};
    string result = "";
    
    for (const auto& roman : romanNums) {
        while (number >= roman.first) {
            number -= roman.first;
            result += roman.second;
        }
        if (!result.empty() && number >= 3 * roman.first) {
            int count = number / roman.first;
            string temp = roman.second;
            for (int i = 1; i < count; i++) {
                temp += roman.second[0];
            }
            result += temp;
            number -= count * roman.first;
        }
    }
    
    return result;
}