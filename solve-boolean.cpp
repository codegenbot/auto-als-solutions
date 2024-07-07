#include <string>
using namespace std;

string solveBoolean(string s) {
    bool result = false;
    for (char c : s) {
        if (c == 't') {
            result = true;
        } else if (c == 'f') {
            result = false;
        } else if (c == '&') {
            if (!result) {
                result = false;
            }
        } else if (c == '|') {
            if (result) {
                result = true;
            }
        }
    }
    return result ? "True" : "False";
}