#include <vector>
#include <stdexcept>

int do_algebra(vector<string> operato, vector<int> operand) {
    int result = 0;
    for (int i = 1; i < operato.size(); i++) {
        if (operato[i] == "+") {
            if(i-1 >= operand.size()) throw runtime_error("Invalid operation");
            result += operand[i-1];
        } else if (operato[i] == "-") {
            if(i-1 >= operand.size()) throw runtime_error("Invalid operation");
            result -= operand[i-1];
        } else if (operato[i] == "*") {
            int temp = 0;
            for (int j = i; j < operato.size(); j++) {
                if (j == i) {
                    temp += operand[j];
                } else if (operato[j] == "+") {
                    if(j-1 >= operand.size()) throw runtime_error("Invalid operation");
                    temp *= operand[j-1];
                } else if (operato[j] == "*") {
                    if(j-1 >= operand.size()) throw runtime_error("Invalid operation");
                    temp *= operand[j-1];
                }
            }
            result += temp;
            i = j - 1; // skip the remaining operators
        } else if (operato[i] == "//") {
            if(i+1 >= operand.size() || i-1 < 0) throw runtime_error("Invalid operation");
            int temp = operand[i-1] / (operand[i+1]);
            result += temp;
            i++; // skip the division operator
        } else if (operato[i] == "**") {
            int temp = 1;
            for (int j = i; j < operato.size(); j++) {
                if (j == i) {
                    temp *= operand[j];
                } else if (operato[j] == "*") {
                    if(j-1 >= operand.size()) throw runtime_error("Invalid operation");
                    temp *= operand[j-1];
                }
            }
            result += temp;
            i = j - 1; // skip the remaining operators
        }
    }
    return result;
}