string words_in_sentence(string sentence) {
    string result = "";
    int count = 0;

    for (int i = 0; i < sentence.size(); i++) {
        if (sentence[i] == ' ') {
            continue;
        }
        bool isPrime = true;
        int wordLen = 0;
        while (i < sentence.size() && sentence[i] != ' ') {
            i++;
            wordLen++;
        }
        for (int j = 2; j * j <= wordLen; j++) {
            if (wordLen % j == 0) {
                isPrime = false;
                break;
            }
        }
        if (isPrime) {
            result += sentence.substr(count, wordLen - 1) + " ";
            count = i;
        }
    }

    return result.substr(0, result.size() - 1);
}