```cpp
#include <vector>
#include <string>

bool isOpen(char c) {
    return c == '(';
}

bool isClose(char c) {
    return c == ')';
}

string match_parens(vector<string> lst) {
    int open = 0, close = 0;
    for (const string& s : lst) {
        for (char c : s) {
            if (isOpen(c)) open++;
            else if (isClose(c)) close++;
        }
    }
    return (open == close) ? "Yes" : "No";
}