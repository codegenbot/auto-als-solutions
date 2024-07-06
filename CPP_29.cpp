```cpp
bool issame(string a, string b) {
    for(int i = 0; i < min(a.length(), b.length()); i++) {
        if(a[i] != b[i])
            return false;
    }
    return true;
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(string s : strings){
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return result;
}