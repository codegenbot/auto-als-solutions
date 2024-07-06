```cpp
#include <vector>
#include <string>

bool isMatch(const std::string& s) {
    int open = 0, close = 0;
    for (char c : s) {
        if (c == '(') open++;
        else if (c == ')') close++;
    }
    return open == close;
}

std::string match_parens(std::vector<std::string> lst) {
    for (const std::string& s : lst) {
        if (!isMatch(s)) return "No";
    }
    return "Yes";
}