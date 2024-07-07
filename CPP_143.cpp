vector<string> split(const string& str) {
    vector<string> tokens;
    size_t pos = 0, last_pos = 0;
    while ((pos = str.find(" ")) != string::npos) {
        tokens.push_back(str.substr(last_pos, pos - last_pos));
        last_pos = pos + 1;
    }
    tokens.push_back(str.substr(last_pos));
    return tokens;
}

string words_in_sentence(string sentence) {
    vector<string> words = split(sentence);
    ostringstream result;
    for (const string& word : words) {
        if (isPrime(word.length())) {
            result << word << " ";
        }
    }
    return result.str();
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}