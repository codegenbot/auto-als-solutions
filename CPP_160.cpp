int do_algebra(vector<string> operator_, vector<int> operand) {
    string expression;
    for (int i = 0; i < operator_.size(); i++) {
        expression += to_string(operand[i]);
        expression += operator_[i];
    }
    expression += to_string(operand.back());
    
    int result = eval(expression.c_str());
    
    return result;
}

long long eval(const char *p) {
    long long x, y;
    while (*p) {
        if (!isdigit(*p)) {
            switch (*p) {
                case '+':
                    y = x;
                    break;
                case '-':
                    y = -x;
                    break;
                case '*':
                    y = x * (x = strtoll(p + 1, 0, 10));
                    p += strlen(&p[1]);
                    break;
                case '/':
                    y = x / (x = strtoll(p + 1, 0, 10));
                    p += strlen(&p[1]);
                    break;
                case '^':
                    y = pow(x, (x = strtoll(p + 1, 0, 10)));
                    p += strlen(&p[1]);
                    break;
            }
        } else {
            x = x * 10 + (*p - '0');
        }
        p++;
    }
    return y;
}