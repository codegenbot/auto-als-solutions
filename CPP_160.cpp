#include <vector>
#include <string>
#include <cctype>
#include <cstdlib>
#include <stdexcept>

int do_algebra(vector<string> operato, vector<int> operand) {
    string expression = "";
    for (int i = 0; i < operato.size(); i++) {
        expression += to_string(operand[i]);
        expression += operato[i];
    }
    expression += to_string(operand.back());
    int result;
    try {
        result = eval(expression.c_str());
    } catch(const std::runtime_error& e) {
        std::cout << "Invalid input: " << e.what() << std::endl;
    }
    return result;
}

long long eval(const char* pExpr) {
    const char* pEnd = NULL;
    long long v = strtoll(pExpr, &pEnd, 10);
    if (*pEnd == '\0') {
        return v;
    } else {
        throw std::runtime_error("Invalid input");
    }
}