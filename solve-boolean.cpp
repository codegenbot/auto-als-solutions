bool evaluateBooleanExpression(const string &expr) {
    stack<char> stk;
    for (char ch : expr) {
        if (ch == 'T' || ch == 'F' || ch == '&' || ch == '|') {
            stk.push(ch);
        }
        if (stk.size() >= 3) {
            char right = stk.top(); stk.pop();
            char op = stk.top(); stk.pop();
            char left = stk.top(); stk.pop();
            bool leftBool = (left == 'T');
            bool rightBool = (right == 'T');
            bool result;
            if (op == '&') {
                result = leftBool && rightBool;
            } else if (op == '|') {
                result = leftBool || rightBool;
            }
            stk.push(result ? 'T' : 'F');
        }
    }
    return stk.top() == 'T';
}

int main() {
    string input;
    cin >> input;
    bool result = evaluateBooleanExpression(input);
    cout << (result ? "True" : "False") << endl;
    return 0;
}