#include <string>
#include <cctype>

std::string solveBoolean(std::string s) {
    bool result = false;
    for (char c : s) {
        if (std::tolower(c) == 't') {
            result = true;
        } else if (std::tolower(c) == 'f') {
            return result ? "True" : "False";
        } else if (c == '&') {
            if (!result) {
                return "False";
            }
        } else if (c == '|') {
            if (result) {
                return "True";
            }
        }
    }
    return result ? "True" : "False";
}