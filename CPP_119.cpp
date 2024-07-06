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

std::vector<std::string> split(const std::string& str) {
    std::vector<std::string> tokens;
    size_t start = 0, end = 0;
    while ((end = str.find(' ', start)) != std::string::npos) {
        tokens.push_back(str.substr(start, end - start));
        start = end + 1;
    }
    tokens.push_back(str.substr(start));
    return tokens;
}

bool matchParens(const std::vector<std::string>& lst) {
    for (const auto& s : lst) {
        if (!isMatch(s)) return false;
    }
    return true;
}

int main() {
    std::vector<std::string> input = split("hello (world) foo (bar)");
    if (matchParens(input))
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;
    return 0;
}