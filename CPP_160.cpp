```
int do_algebra(vector<string> operato, vector<int> operand) {
    int result = 0;
    int i = 0;
    string temp = "";
    
    for (i = 0; i < operato.size(); i++) {
        temp += operato[i];
        if (i < operato.size() - 1) {
            // Add the current operand to the expression
            temp += to_string(operand[i]) + " ";
        }
    }
    
    int j = 0;
    for (j = 0; j < operand.size(); j++) {
        if (j == operand.size() - 1) {
            // Add the last operand to the expression
            temp += to_string(operand[j]);
        } else {
            // Add the current operand to the expression
            temp += to_string(operand[j]) + " ";
        }
    }
    
    int res = evaluate_expression(temp);
    return res;
}

int evaluate_expression(string s) {
    int res = 0;
    stack<int> st;
    stack<string> ops;

    for (int i = 0; i < s.length(); i++) {
        if (isdigit(s[i])) {
            int num = 0;
            while (i < s.length() && isdigit(s[i])) {
                num = num * 10 + (s[i] - '0');
                i++;
            }
            st.push(num);
        } else if (s[i] == '+' || s[i] == '-' || s[i] == '*' || s[i] == '/') {
            while (!ops.empty() && priority(ops.top()) >= priority(s[i])) {
                applyOp(st, ops);
            }
            ops.push(string(1, s[i]));
        }
    }

    while (!ops.empty()) {
        applyOp(st, ops);
    }

    return st.top();
}

int priority(char op) {
    if (op == '+' || op == '-') {
        return 1;
    } else if (op == '*' || op == '/') {
        return 2;
    }
    return 0;
}

void applyOp(stack<int>& st, stack<string>& ops) {
    int b = st.top();
    st.pop();
    int a = st.top();
    st.pop();

    string op = ops.top();
    ops.pop();

    if (op == "+") {
        st.push(a + b);
    } else if (op == "-") {
        st.push(a - b);
    } else if (op == "*") {
        st.push(a * b);
    } else if (op == "/") {
        st.push(a / b);
    }
}