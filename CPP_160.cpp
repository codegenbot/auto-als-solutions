#include <iostream>
#include <vector>
#include <string>
#include <cmath>

int do_algebra(std::vector<std::string> operator_, std::vector<int> operand) {
    int result = operand[0];
    for (int i = 0; i < operator_.size(); i++) {
        if (operator_[i] == "+") {
            result += operand[i + 1];
        } else if (operator_[i] == "-") {
            result -= operand[i + 1];
        } else if (operator_[i] == "*") {
            result *= operand[i + 1];
        } else if (operator_[i] == "//") {
            if(operand[i+1]!=0)
                result = result / operand[i + 1];
            else
                return -1; // error: division by zero
        } else if (operator_[i] == "**") {
            result = pow(result, operand[i + 1]);
        }
    }
    return result;
}

int main() {
    assert (do_algebra({"//", "*"}, {7, 3, 4}) == 8);
    return 0;
}