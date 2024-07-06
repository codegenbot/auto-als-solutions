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

std::vector<std::string> split(const std::string& str, const std::string& delimitingString) {
    size_t pos = 0, lastPos = 0;
    std::vector<std::string> res;

    while ((pos = str.find(delimitingString, lastPos)) != std::string::npos) {
        res.push_back(str.substr(lastPos, pos - lastPos));
        lastPos = pos + delimitingString.size();
    }

    res.push_back(str.substr(lastPos));

    return res;
}