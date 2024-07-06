#include <string>
#include <vector>

bool matchParens(std::vector<std::string> lst) {
    int open = 0, close = 0;
    for (const std::string& s : lst) {
        for (char c : s) {
            if (c == '(') open++;
            else if (c == ')') close++;
        }
    }
    return open == close;
}

int main() {
    // Your test cases
    std::vector<std::string> list1 = {"(a)", "(b)"};
    std::vector<std::string> list2 = {")("};

    if (matchParens(list1))
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;

    if (matchParens(list2))
        std::cout << "Yes" << std::endl;
    else
        std::cout << "No" << std::endl;

    return 0;
}