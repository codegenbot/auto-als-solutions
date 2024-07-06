string sort_numbers(string numbers) {
    map<string, int> numMap = {{"zero", 0}, {"one", 1}, {"two", 2}, {"three", 3},
        {"four", 4}, {"five", 5}, {"six", 6}, {"seven", 7}, {"eight", 8}, {"nine", 9}};
    vector<string> numVector;
    string token;
    int count = 0;

    for (int i = 0; i < numbers.length(); i++) {
        if (numbers[i] == ' ') {
            continue;
        }
        if (count == 0) {
            token = "";
            while (i < numbers.length() && numbers[i] != ' ') {
                token += numbers[i];
                i++;
            }
            i--; // backtrack
        } else {
            token = numbers.substr(count, i - count);
            count = i + 1;
        }

        if (!numMap.count(token)) {
            return "Invalid input";
        }
        numVector.push_back(token);

    }

    sort(numVector.begin(), numVector.end());

    string output = "";
    for (int i = 0; i < numVector.size(); i++) {
        output += numVector[i] + " ";
    }
    return output;
}