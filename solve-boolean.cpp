Here is the corrected code:

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
            }
            string result = (operand1 == "T" && operand2 == "T") ? "T" : "F";
            operands.push(result);
            operators.push('&');
        } else if (expression[i] == '|') {
            string operand1 = operands.top();
            operands.pop();
            string operand2;
            while (!operators.empty() && operators.top() != '&') {
                operators.pop();
            }
            if (operators.empty()) {
                operand2 = "T";
            } else {
                operand2 = operands.top();
                operands.pop();
            }
            string result = (operand1 == "T" || operand2 == "T") ? "T" : "F";
            operands.push(result);
            operators.push('|');
        } else if (expression[i] == 't' || expression[i] == 'T') {
            operands.push("T");
        } else if (expression[i] == 'f' || expression[i] == 'F') {
            operands.push("F");
        }
    }

    return operands.top() == "T";
}