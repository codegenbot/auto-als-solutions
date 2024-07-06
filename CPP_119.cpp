#include <vector>
#include <string>

bool matchParens(const std::vector<std::string>& lst) {
    int open = 0, close = 0;
    for (const auto& s : lst) {
        for (auto c : s) {
            if (c == '(') open++;
            else close++;
        }
    }
    return open == close;
}