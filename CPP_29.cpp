#include <vector>
#include <string>

bool issame(vector<string> a, vector<string> b) {
    return a == b;
}

vector<string> filter_by_prefix(vector<string> strings, string prefix){
    vector<string> result;
    for (string s : strings) {
        if (issame({s.substr(0, prefix.length())}, {prefix}))
            result.push_back(s);
    }
    return result;
}