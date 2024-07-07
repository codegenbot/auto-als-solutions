vector<int> indicesOfSubstring(string text, string target) {
    vector<int> result;
    for (int i = 0; ; i++) {
        int j = i + 1;
        while (j <= text.length() && text.substr(i, j - i).compare(target) != 0) {
            if (j > text.length()) break;
            j++;
        }
        if (j > text.length()) break;
        result.push_back(i);
    }
    return result;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}