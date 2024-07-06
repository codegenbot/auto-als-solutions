bool issame(string a, string b) {
    return (a.size() == b.size()) && (a.compare(b) == 0);
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(string s : strings){
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return result;
}