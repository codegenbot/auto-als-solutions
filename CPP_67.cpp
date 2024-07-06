int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0;
    int oranges = 0;

    // Find the position of "apples" and count the number of apples.
    while ((pos = s.find(" apples", pos)) != string::npos) {
        if (pos + 8 <= s.length()) {
            int start = pos;
            while (s[start] >= '0' && s[start] <= '9') start++;
            int end = start;
            while (end < s.length() && s[end] >= '0' && s[end] <= '9') end++;
            apples = stoi(s.substr(start, end - start));
        }
        pos += 8;
    }

    // Find the position of "oranges" and count the number of oranges.
    while ((pos = s.find(" oranges", pos)) != string::npos) {
        if (pos + 8 <= s.length()) {
            int start = pos;
            while (s[start] >= '0' && s[start] <= '9') start++;
            int end = start;
            while (end < s.length() && s[end] >= '0' && s[end] <= '9') end++;
            oranges = stoi(s.substr(start, end - start));
        }
        pos += 8;
    }

    // Calculate the total number of fruits and return the difference.
    int totalFruits = n;
    if (totalFruits > apples + oranges) {
        return totalFruits - apples - oranges;
    } else {
        return 0;
    }
}