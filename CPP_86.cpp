#include <algorithm>

string anti_shuffle(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ') {
            result += " ";
        } else {
            string word;
            bool firstChar = true;
            for (int j = i; j < s.length() && s[j] != ' '; j++) {
                if (!firstChar) {
                    result += to_string((int)s[j]) + "";
                }
                firstChar = false;
                word += s[j];
            }
            i = j - 1;
            for (char c : word) {
                result += c;
            }
        }
    }
    return result;
}