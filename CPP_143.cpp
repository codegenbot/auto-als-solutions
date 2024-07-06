string words_in_sentence(string sentence){
    string result = "";
    int count = 0;
    for(int i = 0; i < sentence.size(); i++){
        if(sentence[i] == ' ' || i == sentence.size() - 1){
            string word = sentence.substr(count, i - count);
            if(isPrime(word.length())){
                result += word + " ";
            }
            count = i+1;
        }
    }
    return result.substr(0, result.size()-1);
}

bool isPrime(int n) {
    if (n <= 1)
        return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0)
            return false;
    return true;
}