#include <string>

std::string solve(std::string s) {
    std::string result = "";
    bool foundLetter = false;

    for (char c : s) {
        if (!isalpha(c)) {
            result += c;
            foundLetter = false;
        } else {
            if (!foundLetter) {
                foundLetter = true;
                result += tolower(c);
            } else {
                result += toupper(c);
            }
        }
    }

    if (!foundLetter) {
        reverse(result.begin(), result.end());
    }

    return result;
}