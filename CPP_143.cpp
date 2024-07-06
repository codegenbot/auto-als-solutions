string words_in_sentence(string sentence){
    string result = "";
    for (int i = 0; i < sentence.size(); ++i) {
        if (sentence[i] == ' ') continue;
        int len = 1;
        for (int j = i+1; j <= sentence.size() && j != i; ++j) {
            if (sentence[j] != ' ') len++;
            else break;
        }
        bool isPrime = true;
        for (int k = 2; k * k <= len; ++k) {
            if (len % k == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) result += sentence.substr(i, len) + " ";
    }
    return result;
}