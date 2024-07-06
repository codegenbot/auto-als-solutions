string anti_shuffle(string s){
    string result = "";
    size_t pos = 0;
    while((pos = s.find(' ')) != string::npos) {
        string word = s.substr(0, pos);
        string newWord = "";
        for(char c : word) {
            if(find(newWord.begin(), newWord.end(), c) == newWord.end()) {
                newWord += c;
            }
        }
        result += newWord + " ";
        s.erase(0, pos+1);
    }
    result += s;
    return result;
}