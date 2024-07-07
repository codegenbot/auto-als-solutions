#include <iostream>
#include <vector>
#include <string>

using namespace std;

int do_algebra(vector<string> operato, vector<int> operand) {
    int result = 0;
    for (int i = 1; i < operato.size(); i++) {
        if (operato[i] == "+") {
            result += operand[i-1];
        } else if (operato[i] == "-") {
            result -= operand[i-1];
        } else if (operato[i] == "*") {
            int temp = 1;
            for (int j = i; j < operato.size(); j++) {
                if (j == i) {
                    temp *= operand[j];
                } else if (operato[j] == "+") {
                    temp *= operand[j-1];
                } else if (operato[j] == "*") {
                    temp *= operand[j-1];
                }
            }
            result += temp;
            i = j - 1; // skip the remaining operators
        } else if (operato[i] == "//") {
            int temp = operand[i-1] / operand[i+1];
            result += temp;
            i++; // skip the division operator
        } else if (operato[i] == "**") {
            int temp = 1;
            for (int j = i; j < operato.size(); j++) {
                if (j == i) {
                    temp *= operand[j];
                } else if (operato[j] == "*") {
                    temp *= operand[j-1];
                }
            }
            result += temp;
            i = j - 1; // skip the remaining operators
        }
    }
    return result;
}

int main() {
    assert (do_algebra({"//", "*"}, {7, 3, 4}) == 8);
    return 0;
}