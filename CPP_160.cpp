int do_algebra(vector<string> operator_, vector<int> operand) {
    int result = 0;
    for (int i = 1; i < operand.size(); i++) {
        if (*operator_.begin() == "+") {
            result += operand[i];
        } else if (*operator_.begin() == "-") {
            result -= operand[i];
        } else if (*operator_.begin() == "*") {
            result *= operand[i];
        } else if (*operator_.begin() == "//") {
            result /= (operand[i] + 0.5);
        } else if (*operator_.begin() == "**") {
            result = pow(operand[0], operand[i]);
        }
        operator_.erase(operator_.begin());
    }
    return result;
}