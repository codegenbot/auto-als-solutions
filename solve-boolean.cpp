#include <string>

bool solveBoolean(std::string s) {
    bool result = false;
    for (char c : s) {
        if (c == 'T' || c == 't') {
            result = true;
        } else if (c == 'F' || c == 'f') {
            return !result;
        } else if (c == '&') {
            if (!result) {
                return false;
            }
        } else if (c == '|') {
            if (result) {
                return true;
            }
        }
    }
    return result;
}