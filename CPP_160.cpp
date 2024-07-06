#include <vector>
#include <string>

using namespace std;

int do_algebra(vector<string> operator_, vector<int> operands) {
    int result = operands[0];
    for (int i = 0; i < operator_.size(); i++) {
        string op = operator_[i];
        if (op == "+") {
            result += operands[i + 1];
        } else if (op == "-") {
            result -= operands[i + 1];
        } else if (op == "*") {
            result *= operands[i + 1];
        } else if (op == "//") {
            result /= operands[i + 1];
        } else if (op == "**") {
            result = pow(result, operands[i + 1]);
        }
    }
    return result;
}