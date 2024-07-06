#include <stack>

vector<int> parse_nested_parens(string paren_string) {
    vector<int> result;
    stack<int> levels;
    int maxLevel = 0;

    for (char c : paren_string) {
        if (c == '(') {
            levels.push(1);
            maxLevel = max(maxLevel, 1);
        } else if (c == ')') {
            levels.pop();
            maxLevel = max(maxLevel, levels.size());
        }
    }

    while (!levels.empty()) {
        result.push_back(maxLevel);
        levels.pop();
    }

    return result;
}