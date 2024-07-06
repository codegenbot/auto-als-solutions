int do_algebra(vector<string> operator_, vector<int> operand) {
    int result = operand[0];
    string op;
    
    for (int i = 1; i < operator_.size() + 1; ++i) {
        if (operator_[i-1] == "+") {
            result += operand[i];
        } else if (operator_[i-1] == "-") {
            result -= operand[i];
        } else if (operator_[i-1] == "*") {
            result *= operand[i];
        } else if (operator_[i-1] == "//") {
            result = result / static_cast<int>(operand[i]);
        } else if (operator_[i-1] == "**") {
            result = pow(result, operand[i]);
        }
    }
    
    return result;
}