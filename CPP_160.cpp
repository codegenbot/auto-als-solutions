int do_algebra(vector<string> operator, vector<int> operand) {
    int result = 0;
    for (int i = 0; i < operator.size(); i++) {
        if (operator[i] == "+") {
            result += operand[i];
        } else if (operator[i] == "-") {
            result -= operand[i];
        } else if (operator[i] == "*") {
            int temp = result;
            result = 0;
            for (int j = i; j < operand.size(); j++) {
                result += temp * operand[j];
            }
        } else if (operator[i] == "//") {
            result /= operand[i];
        } else if (operator[i] == "**") {
            int temp = 1;
            for (int j = i; j < operand.size(); j++) {
                temp *= pow(operand[j], result);
            }
            result = temp;
        }
    }
    return result;
}