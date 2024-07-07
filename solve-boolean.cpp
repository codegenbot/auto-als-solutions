#include <string>

std::string solveBoolean(std::string s) {
    bool result = false;
    for (char c : s) {
        if (c == 'T') {
            result = true;
        } else if (c == 'F') {
            return "False";
        } else if (c == '&') {
            if (!result) {
                return "False";
            }
            result &= true;
        } else if (c == '|') {
            if (result) {
                return "True";
            }
            result |= true;
        }
    }
    return result ? "True" : "False";
}