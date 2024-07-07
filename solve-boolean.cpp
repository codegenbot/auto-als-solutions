#include <string>
#include <iostream>

bool solveBoolean(std::string s) {
    bool result = false;
    for (char c : s) {
        if (c == 't') {
            result = true;
        } else if (c == 'f') {
            return !result;
        } else if (c == '|') {
            if (!result) {
                return true;
            }
        } else if (c == '&') {
            if (result) {
                return true;
            } else {
                return false;
            }
        }
    }
    return result;
}