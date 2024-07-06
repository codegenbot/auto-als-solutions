map<string, int> numMap = {
    {"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
    {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7},
    {"eight", 8}, {"nine", 9}
};

string sort_numbers(string numbers) {
    vector<string> numVec;
    size_t pos = 0;
    while ((pos = numbers.find(" ")) != string::npos) {
        string num = numbers.substr(0, pos);
        numbers.erase(0, pos + 1);
        numVec.push_back(num);
    }
    numVec.push_back(numbers);

    sort(numVec.begin(), numVec.end(),
         [&numMap](const string& a, const string& b) {
             return numMap.at(a) < numMap.at(b);
         });

    string result;
    for (const auto& num : numVec) {
        result += num + " ";
    }
    return result;
}