#include <string>
#include <algorithm>
using namespace std;

string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = toupper(c);
            if (c == 'O' || c == 'o') {
                c = 'Q';
            } else if (c == 'U' || c == 'u') {
                c = 'W';
            }
            result += c;
        } else {
            result += c;
        }
    }
    transform(result.begin(), result.end(), result.begin(), ::tolower);
    return result;
}