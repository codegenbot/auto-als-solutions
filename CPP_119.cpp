#include <string>
#include <vector>

bool isMatched(const std::vector<std::string>& lst) {
    int open = 0, close = 0;
    for (const auto& s : lst) {
        for (auto c : s) {
            if (c == '(') open++;
            else if (c == ')') close++;
        }
    }
    return open == close;
}

int main() {
    std::vector<std::string> lst = {"(hello)", "world", "(goodbye)"};
    if (isMatched(lst)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}