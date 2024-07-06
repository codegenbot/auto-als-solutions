int fruit_distribution(string s, int n) {
    size_t pos = 0;
    string apples = "apples";
    string oranges = "oranges";

    // Find the number of apples
    pos = s.find(apples);
    int appleCount = 0;
    if (pos != string::npos) {
        int start = pos + apples.length();
        while (start < s.length() && isdigit(s[start])) {
            appleCount = appleCount * 10 + (s[start] - '0');
            start++;
        }
    }

    // Find the number of oranges
    pos = s.find(oranges);
    int orangeCount = 0;
    if (pos != string::npos) {
        int start = pos + oranges.length();
        while (start < s.length() && isdigit(s[start])) {
            orangeCount = orangeCount * 10 + (s[start] - '0');
            start++;
        }
    }

    return n - appleCount - orangeCount;
}