bool issame(string a, string b) {
    vector<string> result;
    for(string s : {a, b}) {
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return !result.empty();
}