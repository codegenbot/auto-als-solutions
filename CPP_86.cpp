string anti_shuffle(string s){
    string result = "";
    for(auto word : split(s, " ")){
        string temp = "";
        for(auto c : word){
            temp += (temp.empty() ? "" : " ") + c;
        }
        result += temp + " ";
    }
    return result.substr(0, result.size()-1);
}

string split(const string& str, const string& delimiter) {
    size_t pos = 0;
    string token;
    std::vector<string> tokens;
    while ((pos = str.find(delimiter)) != std::string::npos) {
        token = str.substr(0, pos);
        str.erase(0, pos + delimiter.length());
        tokens.push_back(token);
    }
    tokens.push_back(str);
    return tokens.size() > 1 ? tokens : vector<string>(1, str);
}