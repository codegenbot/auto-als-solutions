string words_in_sentence(string sentence){
    string result = "";
    for(string word : split(sentence, ' ')){
        if(is_prime(word.length())){
            result += word + " ";
        }
    }
    return result.substr(0, result.size()-1);
}

vector<string> split(string str, char ch) {
    vector<string> ar;
    size_t pos = 0;
    while((pos = str.find(ch)) != string::npos) {
        ar.push_back(str.substr(0, pos));
        str.erase(0, pos + 1);
    }
    ar.push_back(str);
    return ar;
}

bool is_prime(int num){
    if(num <= 1) return false;
    for(int i = 2; i*i <= num; i++){
        if(num%i == 0) return false;
    }
    return true;
}