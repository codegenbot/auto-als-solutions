string solveBoolean(string expression) {
    stack<char> s;
    for (int i = 0; i < expression.length(); ++i) {
        if (expression[i] == '&') {
            s.push(expression[i]);
            i++;
            while(i < expression.length() && expression[i] != '|') {
                i++;
            }
        } else if (expression[i] == '|') {
            while(!s.empty()) {
                s.pop();
            }
        }
    }
    string result = "";
    while (!s.empty()) {
        result += s.top();
        s.pop();
    }
    return result;
}