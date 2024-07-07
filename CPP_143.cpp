string words_in_sentence(string sentence){
    string result = "";
    int count = 0;
    for (int i = 0; i < sentence.size(); i++) {
        if (sentence[i] == ' ') {
            continue;
        }
        bool isPrime = true;
        int len = 0;
        for (int j = i; j < sentence.size() && sentence[j] != ' '; j++, len++) {
            len++;
            if (len > 1 && !isPrime(len)) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            result += &sentence[i] - &sentence[0];
            i += len - 1;
            count++;
        }
    }
    return result;
}

bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i * i <= num; i++)
        if (num % i == 0)
            return false;
    return true;
}