#include <algorithm>
#include <sstream>

using namespace std;

string anti_shuffle(string s) {
    stringstream ss(s);
    string word;
    string result = "";

    while (ss >> word) {
        for (char c : word) {
            result += c;
        }
        for (int i = 0; i < word.length(); ++i) {
            char c = word[i];
            for (int j = i + 1; j < word.length(); ++j) {
                if (c > word[j]) {
                    swap(c, word[j]);
                }
            }
            result += c;
        }
        result += " ";
    }

    return result.substr(0, result.length() - 1);
}