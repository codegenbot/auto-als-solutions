Here is the completed code:

map<char, int> histogram(string test) {
    map<char, int> result;
    if (test.empty()) return result;

    size_t pos = 0;
    while ((pos = test.find(' ')) != string::npos) {
        char c = test[0];
        int count = 1;
        while (pos > 0 && test[pos - 1] == c) {
            pos = test.find(' ', pos);
            if (pos == string::npos) break;
            pos++;
            count++;
        }
        result[c] = count;
        test.erase(0, pos);
    }

    // handle the remaining characters
    char c = test[0];
    int count = 1;
    while (test.size() > 1 && test[1] == c) {
        test.erase(0, 1);
        count++;
    }
    if (!test.empty()) result[c] = count;

    return result;
}