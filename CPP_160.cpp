```cpp
int do_algebra(vector<string> operato, vector<int> operand) {
    int result = operand[0];
    for (int i = 0; i < operato.size(); i++) {
        if (operato[i] == "+") {
            result += operand[i + 1];
        } else if (operato[i] == "-") {
            result -= operand[i + 1];
        } else if (operato[i] == "*") {
            result *= operand[i + 1];
        } else if (operato[i] == "///") {
            result = result / operand[i + 1]; // Floor division
        } else if (operato[i] == "**") {
            result = pow(operand[0], operand[i + 1]); // Raise the first operand to the power of the second
        }
    }
    return result;
}