#include <string>
#include <vector>

bool isOpen(char c) {
    return c == '(';
}

bool isClose(char c) {
    return c == ')';
}

int countOpen(const std::vector<std::string>& lst) {
    int count = 0;
    for (const auto& s : lst) {
        for (char c : s) {
            if (isOpen(c)) {
                count++;
            }
        }
    }
    return count;
}

bool matchParens(const std::vector<std::string>& lst) {
    int open = countOpen(lst);
    int close = lst.size() - open;
    return open == close;
}

int main() {
    std::vector<std::string> lst = {"(a)", "b(c)"};
    if (matchParens(lst)) {
        std::cout << "Yes" << std::endl;
    } else {
        std::cout << "No" << std::endl;
    }
    return 0;
}