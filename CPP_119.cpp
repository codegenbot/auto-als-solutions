```cpp
#include <string>
#include <vector>

bool check(char c) {
    if (c == '(') return true;
    else return false;
}

string match_parens(vector<string> lst) {
    int open = 0, close = 0;
    for (const string& s : lst) {
        for (char c : s) {
            if (check(c)) open++;
            else close++;
        }
    }
    return (open == close) ? "Yes" : "No";
}