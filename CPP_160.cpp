#include <iostream>
#include <vector>
#include <cmath>

int do_algebra(vector<string> operato, vector<int> operand) {
    int result = operand[0];
    for (int i = 0; i < operato.size(); i++) {
        if (operato[i] == "+") {
            if(i+1<operand.size()) {
                result += operand[i + 1];
            }
        } else if (operato[i] == "-") {
            if(i+1<operand.size()) {
                result -= operand[i + 1];
            }
        } else if (operato[i] == "*") {
            if(i+1<operand.size()) {
                result *= operand[i + 1];
            }
        } else if (operato[i] == "//") {
            if(i+1<operand.size() && operand[i+1]!=0) {
                result = result / operand[i + 1];
            }
        } else if (operato[i] == "**") {
            if(i+1<operand.size()) {
                result = pow(result, operand[i + 1]);
            }
        }
    }
    return result;
}

int main() {
    assert (do_algebra({"//", "*"}, {7, 3, 4}) == 8);
}