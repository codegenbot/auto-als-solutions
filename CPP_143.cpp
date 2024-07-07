string words_in_sentence(string sentence){
    string result = "";
    for (int i = 0; i < sentence.size(); ++i) {
        int j = i;
        while(sentence[j] != ' ') {
            j++;
        }
        string word = sentence.substr(i, j-i);
        if(is_prime(word.length())) {
            result += word + " ";
        }
        i = j;
    }
    return result;
}

bool is_prime(int n) {
    if(n <= 1)
        return false;
    for (int i = 2; i * i <= n; ++i) {
        if(n % i == 0)
            return false;
    }
    return true;
}