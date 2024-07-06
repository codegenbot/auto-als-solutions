vector<int> primeNumbers(int n) {
    vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        bool isPrime = true;
        for (int j = 2; j * j <= i; ++j) {
            if (i % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            primes.push_back(i);
        }
    }
    return primes;
}

string words_in_sentence(string sentence){
    vector<string> words;
    split(sentence, " ", words);

    string result = "";
    for (const auto &word : words) {
        int length = word.length();
        if (any_of(primeNumbers(length).begin(), primeNumbers(length).end(),
            [&length](int i) { return i == length; })) {
            result += word + " ";
        }
    }

    return result.substr(0, result.size() - 1);
}