#include <algorithm>
using namespace std;

string anti_shuffle(string s) {
    string result = "";
    for (const auto& word : split(s, " ")) {
        result += anti_sort(word) + " ";
    }
    return result.substr(0, result.size() - 1);
}

string anti_sort(const string& str) {
    string result;
    for (char c : str) {
        if (!result.empty() && result.back() <= c)
            continue;
        result += c;
    }
    return result;
}

vector<string> split(const string& s, const string& delimiter) {
    vector<string> result;
    size_t pos = 0, prev = 0;
    while ((pos = s.find(delimiter, prev)) != string::npos) {
        result.push_back(s.substr(prev, pos - prev));
        prev = pos + delimiter.size();
    }
    result.push_back(s.substr(prev));
    return result;
}