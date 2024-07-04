bool evaluateBooleanExpression(const string &expr) {
    stack<char> st;
    for (char ch : expr) {
        if (ch == 'T' || ch == 'F' || ch == '&' || ch == '|') {
            st.push(ch);
        }
        if (st.size() >= 3) {
            char b = st.top(); st.pop();
            char op = st.top(); st.pop();
            char a = st.top(); st.pop();
            if (op == '&') {
                st.push((a == 'T' && b == 'T') ? 'T' : 'F');
            } else if (op == '|') {
                st.push((a == 'T' || b == 'T') ? 'T' : 'F');
            }
        }
    }
    return st.top() == 'T';
}

int main() {
    string expr;
    cin >> expr;
    bool result = evaluateBooleanExpression(expr);
    cout << (result ? "True" : "False") << endl;
    return 0;
}