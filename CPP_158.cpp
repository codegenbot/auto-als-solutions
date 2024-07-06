string find_max(vector<string> words){
    string res = words[0];
    for (const auto& word : words) {
        if (word.length() > res.length()) {
            res = word;
        } else if (word.length() == res.length()) {
            if (res < word) {
                res = word;
            }
        }
    }
    return res;
}