```cpp
#include <vector>
#include <string>

bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    return a == b;
}

std::vector<std::string> split_words(string txt) {
    vector<string> result = {};
    size_t pos = 0;
    while ((pos = txt.find(' ')) != string::npos) {
        result.push_back(txt.substr(0, pos));
        txt.erase(0, pos + 1);
    }
    if (txt.empty()) {
        return result;
    }
    result.push_back(txt);
    return result;
}