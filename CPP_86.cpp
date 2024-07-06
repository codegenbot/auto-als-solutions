#include <algorithm>
using namespace std;

string anti_shuffle(string s) {
    string result = "";
    for (const auto& word : split(s, ' ')) {
        for (char c : word) {
            result += (c <= 'z' && c >= 'a') ? c : ' ';
        }
        result += " ";
    }
    return result;
}

string split(const string& str, char delimiter) {
    string result = "";
    size_t pos = 0;
    while ((pos = str.find(delimiter)) != std::string::npos) {
        result += str.substr(0, pos);
        str.erase(0, pos + 1);
    }
    result += str;
    return result;
}