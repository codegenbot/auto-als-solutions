map<char, int> histogram(string test) {
    map<char, int> result;
    if (test.empty()) return result;

    size_t pos = 0;
    char letter;
    int count = 0;

    while ((pos = test.find(' ')) != string::npos) {
        letter = test[0];
        count++;
        test.erase(0, pos + 1);
    }

    if (!test.empty()) {
        letter = test[0];
        count++;
    }

    result[letter] = count;

    return result;
}