int do_algebra(vector<string> operator, vector<int> operand) {
    string expression = "";
    for (int i = 0; i < operator.size(); i++) {
        expression += to_string(operand[i]);
        expression += operator[i];
    }
    expression += to_string(operand.back());
    
    int result = eval(expression.c_str());
    return result;
}

long long eval(const char *p) {
    long long v = 0;
    while (*p) {
        if (isdigit(*p)) {
            v = v * 10 + (*p - '0');
        } else if (*p == '(') {
            v = eval(++p);
            p = strchr(p, ')');
            if (!p) throw runtime_error("Mismatched parentheses");
            *p++ = '\0';
        } else if (*p in "+-*/") {
            ++p;
        }
    }
    return v;
}