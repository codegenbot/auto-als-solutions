```cpp
vector<int> parse_nested_parens(string paren_string) {
    vector<int> result;
    stack<int> nesting_levels(0);
    for (char c : paren_string) {
        if (c == '(') {
            nesting_levels.push(1 + nesting_levels.top());
        } else if (c == ')') {
            result.push_back(nesting_levels.top());
            nesting_levels.pop();
        }
    }
    return result;
}