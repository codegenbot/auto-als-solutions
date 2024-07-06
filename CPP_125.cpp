bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::vector<std::string>> split_words(string txt) {
    vector<vector<string>> result = {};
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        vector<string> temp = {};
        for(int i = 0; i <= pos; i++) {
            if(i < txt.length()) {
                temp.push_back(txt.substr(0, i+1));
                txt.erase(0, i+1);
            }
        }
        result.push_back(temp);
    }
    if (!txt.empty()) {
        vector<string> temp = {};
        for(int i = 0; i <= txt.length(); i++) {
            if(i < txt.length()) {
                temp.push_back(txt.substr(0, i+1));
                txt.erase(0, i+1);
            }
        }
        result.push_back(temp);
    }
    return result;
}