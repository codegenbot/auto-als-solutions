```cpp
#include <vector>
#include <string>

bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (string s : strings) {
        if (issame({split(s, prefix)}, {split(prefix, "")}))
            result.push_back(s);
    }
    return result;
}

vector<string> split(string s, string prefix) {
    vector<string> res;
    size_t found = 0;
    while((found = s.find(prefix)) != string::npos) {
        res.push_back(s.substr(0, found));
        s.erase(0, found + prefix.length());
    }
    res.push_back(s);
    return res;
}