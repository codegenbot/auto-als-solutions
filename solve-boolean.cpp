#include <string>

using namespace std;

string solveBoolean(string s) {
    bool result = false;
    for (char c : s) {
        if (c == 'T') result = true;
        else if (c == 'F') return "False";
        else if (c == '&') {
            if (!result) return "False";
        }
        else if (c == '|') {
            if (result) return "True";
            else result = true;
        }
    }
    return result ? "True" : "False";