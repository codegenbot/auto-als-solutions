bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<std::vector<std::string>> split_words(string txt) {
    vector<vector<string>> result = {{}};
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        vector<string> temp = {};
        temp.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
        if (!result.empty()) {
            result.back().push_back(txt);
            break;
        }
        result.push_back(temp);
    }
    if (txt.empty()) {
        return result;
    }
    vector<string> temp = {};
    temp.push_back(txt);
    result.push_back(temp);
    return result;
}