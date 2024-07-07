#include <string>
using namespace std;

bool evaluateBooleanExpression(string expression) {
    stack<char> operatorStack;
    string temp = "";
    
    for (int i = 0; i < expression.length(); i++) {
        if (expression[i] == '&' || expression[i] == '|') {
            while (!operatorStack.empty() && operatorStack.top() != '(') {
                if (operatorStack.top() == '&')
                    temp += '&';
                else
                    temp += '|';
                operatorStack.pop();
            }
            operatorStack.pop(); // Pop the '('
            if (!temp.empty()) {
                if (expression[i] == '&') 
                    temp += '&';
                else
                    temp += '|';
                temp += ' ';
            }
            temp += expression[i];
        } else if (expression[i] == '(') {
            operatorStack.push(expression[i]);
            temp += expression[i];
        } else if (expression[i] == ')') {
            while (!operatorStack.empty() && operatorStack.top() != '(') {
                if (operatorStack.top() == '&')
                    temp += '&';
                else
                    temp += '|';
                operatorStack.pop();
            }
            operatorStack.pop(); // Pop the '('
        } else {
            temp += expression[i];
        }
    }
    
    while (!operatorStack.empty()) {
        if (operatorStack.top() == '&')
            temp += '&';
        else
            temp += '|';
        operatorStack.pop();
    }
    
    int i = 0;
    while (i < temp.length() && temp[i] != ' ') 
        i++;
    temp = temp.substr(i);
    
    bool result = (temp == "t") ? true : ((temp == "f") ? false : false);
    
    return result;
}