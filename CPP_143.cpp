string words_in_sentence(string sentence) {
    string result = "";
    vector<int> primeNumbers;
    for (int i = 2; i <= 100; i++) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; j++) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime)
            primeNumbers.push_back(i);
    }

    vector<string> words = split(sentence, ' ');
    for (string word : words) {
        if (find(primeNumbers.begin(), primeNumbers.end(), word.length()) != primeNumbers.end())
            result += word + " ";
    }
    return result.substr(0, result.size() - 1);
}

vector<string> split(const string& str, char ch) {
    vector<string> tokens;
    size_t pos = 0;
    while ((pos = str.find(ch)) != string::npos) {
        tokens.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }
    tokens.push_back(str);
    return tokens;
}