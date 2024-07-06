#include <algorithm>
#include <sstream>

using namespace std;

string anti_shuffle(string s) {
    stringstream ss(s);
    string word;
    string result = "";

    while (getline(ss, word, ' ')) {
        result += "#";
        for (char c : word) {
            if (!result.empty() && result.back() == '#') {
                result.pop_back();
            }
            result += (char)tolower(c);
        }
        result += " ";
    }

    return result.substr(0, result.size() - 1); // Remove the last space
}