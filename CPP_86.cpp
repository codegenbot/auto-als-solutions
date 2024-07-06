#include <algorithm>
#include <string>

using namespace std;

string anti_shuffle(string s) {
    string result = "";
    for (const auto& word : split(s, " ")) {
        for (char c : word) {
            if (!result.empty()) {
                result += " ";
            }
            for (int i = 0; i < c; i++) {
                result += static_cast<char>(i);
            }
            result += c;
        }
    }
    return result;
}

string split(const string& s, const string& delimiter) {
    size_t pos = 0;
    string token;
    vector<string> tokens;
    while ((pos = s.find(delimiter)) != string::npos) {
        token = s.substr(0, pos);
        tokens.push_back(token);
        s.erase(0, pos + delimiter.length());
    }
    tokens.push_back(s);
    return join(tokens, " ");
}

string join(const vector<string>& tokens, const string& delimiter) {
    string result;
    for (const auto& token : tokens) {
        if (!result.empty()) {
            result += delimiter;
        }
        result += token;
    }
    return result;
}