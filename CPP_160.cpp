int do_algebra(vector<string> operator_, vector<int> operand) {
    int result = operand[0];
    string opstr = "";
    for (int i = 1; i < operator_.size(); i++) {
        opstr += operator_[i];
        result = eval(result, opstr, &operand[i]);
        opstr.clear();
    }
    return result;
}

long long eval(int a, const string& op, int b) {
    if (op == "+")
        return a + b;
    else if (op == "-")
        return a - b;
    else if (op == "*")
        return a * b;
    else if (op == "//")
        return a / b;
    else
        return pow(a, b);
}