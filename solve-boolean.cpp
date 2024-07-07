#include <string>

std::string solveBoolean(std::string s) {
    bool result = false;
    for (char c : s) {
        if (c == 'T') {
            result = true;
        } else if (c == 'F') {
            return "false";
        } else if (c == '|') {
            if (result) {
                return "true";
            }
        } else if (c == '&') {
            if (!result) {
                return "false";
            }
        }
    }
    return result ? "true" : "false";
}