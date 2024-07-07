#include <stack>
#include <string>

bool evaluateBooleanExpression(string expression) {
    stack<char> operators;
    stack<string> operands;

    for (int i = 0; i < expression.length(); i++) {
        if (expression[i] == '&') {
            string operand1 = operands.top();
            operands.pop();
            string operand2;
            while (!operators.empty() && operators.top() != '|') {
                operators.pop();
            }
            if (operators.empty()) {
                operand2 = "T";
            } else {
                operand2 = operands.top();
                operands.pop();
        #include <string>
