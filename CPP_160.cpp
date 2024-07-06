```cpp
#include <cstddef>
#include <stdexcept>
#include <cmath>

int do_algebra(vector<string> operato, vector<int> operand) {
    string expression = "";
    for (int i = 0; i < operato.size(); i++) {
        expression += to_string(operand[i]);
        expression += operato[i];
    }
    expression += to_string(operand.back());
    int result = eval(expression.c_str());
    return result;
}

long long eval(const char* pExpr) {
    const char* pEnd = NULL;
    double v = strtod(pExpr, &pEnd);
    if (*pEnd == '\0') {
        return (int)v;
    }
    throw runtime_error("Invalid input");
}