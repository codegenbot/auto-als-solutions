```
bool issame(string a, string b){
    bool result = true;
    if(a.size() != b.size())
        result = false;
    else
        for(int i=0; i<a.size(); i++)
            if(a[i] != b[i])
                result = false;
    return result;
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for(string s : strings){
        if(s.find(prefix) == 0)
            result.push_back(s);
    }
    return result;
}