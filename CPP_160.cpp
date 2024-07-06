#include <vector>
using namespace std;

int do_algebra(vector<string> operato, vector<int> operand) {
    int result = operand[0];
    for (int i = 1; i <= operato.size(); i++) {
        if (operato[i - 1] == "+") {
            result += operand[i];
        } else if (operato[i - 1] == "-") {
            result -= operand[i];
        } else if (operato[i - 1] == "*") {
            result *= operand[i];
        } else if (operato[i - 1] == "//") { 
            result /= operand[i]; // this will perform integer division
        }
    }
    return result;
}

int main() {
    assert(do_algebra({"//", "*"}, {7, 3, 4}) == 8);
    return 0;
}