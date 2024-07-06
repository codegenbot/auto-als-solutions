```cpp
bool issame(string a, string b) {
    if(a.size() != b.size())
        return false;
    for(int i = 0; i < a.size(); ++i)
        if(tolower(a[i]) != tolower(b[i]))
            return false;
    return true;
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(string s : strings){
        if(s.find(prefix) == 0 && issame(s.substr(0, prefix.size()), prefix))
            result.push_back(s);
    }
    return result;
}