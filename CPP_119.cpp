```cpp
#include <vector>
#include <string>

bool isMatch(const std::vector<std::string>& lst) {
    int open = 0, close = 0;
    for (const auto& s : lst) {
        for (char c : s) {
            if (c == '(') open++;
            else if (c == ')') close++;
        }
    }
    return open == close;
}

int main() {
    std::vector<std::string> lst = {"(abc)", "(def)"};
    bool result = isMatch(lst);
    std::cout << (result ? "Yes" : "No") << std::endl;
    return 0;
}