#include <string>

bool solveBoolean(string s) {
    bool result = false;
    for (char c : s) {
        if (c == 'T') result = true; 
        else if (c == 'F') return false; 
        else if (c == '&') { 
            if (!result) return false; 
        } 
        else if (c == '|') { 
            if (result) return true;
        }
    }
    return result;
}