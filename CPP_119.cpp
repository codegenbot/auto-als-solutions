#include <vector>
#include <string>

int match_parens(std::vector<std::string> lst) {
    int countOpen = 0;
    int countClose = 0;

    for (const std::string& s : lst) {
        for (char c : s) {
            if (c == '(') {
                countOpen++;
            } else if (c == ')') {
                countClose++;
            }
        }
    }

    if (countOpen == countClose) {
        return 1;
    } else {
        return 0;
    }
}