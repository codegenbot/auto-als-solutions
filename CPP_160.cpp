#include <vector>
#include <cmath>

int do_algebra(vector<string> operator_, vector<int> operands_) {
    int result = 0;
    for (int i = 0; i < operator_.size(); i++) {
        if (operator_[i] == "+") {
            result += operands_[i];
        } else if (operator_[i] == "-") {
            result -= operands_[i];
        } else if (operator_[i] == "*") {
            int temp = 1;
            for (int j = i; j < operands_.size(); j++) {
                temp *= operands_[j];
            }
            result += temp;
        } else if (operator_[i] == "/*" || operator_[i] == "//") {
            int temp = operands_[i];
            for (int j = i + 1; j < operands_.size(); j++) {
                temp /= operands_[j];
            }
            result += temp;
        } else if (operator_[i] == "**") {
            int temp = 1;
            for (int j = i; j < operands_.size(); j++) {
                temp *= pow(operands_[j], 1);
            }
            result += temp;
        }
    }
    return result;
}