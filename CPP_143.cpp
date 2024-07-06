string words_in_sentence(string sentence){
    vector<string> words = split(sentence, ' ');
    string result;
    for(auto word : words) {
        int len = word.length();
        bool is_prime = true;
        if(len > 1) {
            for(int i = 2; i*i <= len; i++) {
                if(len % i == 0) {
                    is_prime = false;
                    break;
                }
            }
            if(is_prime) {
                result += word + " ";
            }
        }
    }
    return result.substr(0, result.length() - 1);
}

vector<string> split(const string& str, char delim){
    vector<string> tokens;
    size_t prev = 0, pos = 0;
    do {
        pos = str.find(delim, prev);
        if(pos == string::npos) pos = str.length();
        string token = str.substr(prev, pos - prev);
        tokens.push_back(token);
        prev = pos + 1;
    } while (pos < str.length());
    return tokens;
}