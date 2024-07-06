```
#include <string>
#include <vector>

using namespace std;

bool is_prime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

vector<string> split(const string& str, const string& delimiter) {
    vector<string> result;
    size_t pos = 0;
    while ((pos = str.find(delimiter)) != std::string::npos) {
        result.push_back(str.substr(0, pos));
        str.erase(0, pos + delimiter.length());
    }
    result.push_back(str);
    return result;
}

string trim(const string& str) {
    int start = 0;
    while (start < str.length() && isspace(str[start])) {
        start++;
    }
    int end = str.length() - 1;
    while (end >= 0 && isspace(str[end])) {
        end--;
    }
    return str.substr(start, end - start + 1);
}

string words_in_sentence(string sentence) {
    string result = "";
    for (const auto& word : split(sentence, " ")) {
        if (is_prime(word.length())) {
            result += word + " ";
        }
    }
    return trim(result);
}