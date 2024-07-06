int do_algebra(vector<string> operator_, vector<int> operand) {
    string expression;
    for (int i = 0; i < operator_.size(); i++) {
        if (i == 0) {
            expression += to_string(operand[i]);
        } else {
            expression += " " + operator_[i] + " ";
            expression += to_string(operand[i]);
        }
    }
    int result = eval(expression.c_str());
    return result;
}

long long eval(const char *s) {
    long long x = 0, y = 1;
    while (*s) {
        if (isdigit(*s)) {
            int power = 0;
            do {
                x += (x * 10 + (*s - '0')) * y;
                s++;
                power++;
            } while (isdigit(*s));
            for (; power > 0; power--) y *= 10;
        } else if (*s == '+') {
            y = 1;
            x++;
        } else if (*s == '-') {
            y = -1;
            x--;
        } else if (*s == '*') {
            long long t = x;
            x = x * y;
            y = t;
        } else if (*s == '/') {
            long long t = x;
            x = x / y;
            y = t;
        }
    }
    return x;
}