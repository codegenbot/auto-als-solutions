#include <string>
using namespace std;

string solveBoolean(string s) {
    bool result = false;
    for (char c : s) {
        if (c == 't') {
            result = true;
        } else if (c == 'f') {
            return "False";
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