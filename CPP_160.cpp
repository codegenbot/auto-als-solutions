int do_algebra(vector<string> operator_, vector<int> operand) {
    string expression = "";
    for (int i = 0; i < operator_.size(); i++) {
        expression += to_string(operand[i]);
        if (i < operator_.size() - 1)
            expression += operator_[i];
    }
    expression += to_string(operand.back());
    
    int result = eval(expression.c_str());
    
    return result;
}

int eval(char* expr) {
    int result = 0;
    char *p = NULL, *q = NULL;
    double tmp = 0.0;

    if (expr[0] == '0' || (expr[0] >= '1' && expr[0] <= '9')) {
        for (; *expr; expr++) {
            if (*expr >= '0' && *expr <= '9') {
                tmp = tmp * 10.0 + (*expr - '0');
            } else if (*expr == '.') {
                p = expr;
            } else if (*expr == 'E' || *expr == 'e') {
                q = expr;
            }
        }
        result = (int)tmp;

    } else {
        result = 0;
    }

    return result;
}