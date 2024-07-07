#include <stack>
#include <limits>

using namespace std;

long long LONG_LONG_MAX = numeric_limits<long long>::max();

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

long long eval(const char* pExpr)
{
    char buff[256];
    const char* pToken;
    long long v;

    // Create a new stack
    stack<long long> valueStack;

    // Process the input string one token at a time:
    while (*pExpr) {
        // Find the next token that begins with * or is a valid number
        pToken = pExpr;
        if (strncasecmp(pToken, "pow(", 4) == 0)
            pToken += 4;
        else if (*pToken == '(') {
            int count = 1;
            while (++pToken, *pToken != ')') {
                if (*pToken == '(')
                    ++count;
            }
            pToken++;
            // Now process the expression inside the parentheses
            v = eval(pToken);
            for (int i = 0; i < count; i++)
                valueStack.push(v);
        } else if (*pToken == '-') {
            v = -1;
            while (*++pToken != ' ') {
                if (*pToken >= '0' && *pToken <= '9')
                    v = v * 10 + (long long)(*pToken - '0');
                else
                    break;
            }
        } else if (*pToken == '+') {
            v = 1;
            while (*++pToken != ' ') {
                if (*pToken >= '0' && *pToken <= '9')
                    v = v * 10 + (long long)(*pToken - '0');
                else
                    break;
            }
        } else if (*pToken == '.') {
            v = 0;
            while (*++pToken != ' ') {
                if (*pToken >= '0' && *pToken <= '9')
                    v = v * 10 + (long long)(*pToken - '0');
                else
                    break;
            }
        } else if (*pToken == 'x') {
            v = 1;
            while (*++pToken != ' ') {
                if (*pToken >= '0' && *pToken <= '9')
                    v = v * 10 + (long long)(*pToken - '0');
                else
                    break;
            }
        } else {
            pToken++;
            // Skip any spaces or parentheses:
            while (*pToken == ' ')
                ++pToken;
            if (*pToken == '(')
                pToken++;
            v = 0;
            while (*pToken >= '0' && *pToken <= '9') {
                v = v * 10 + (long long)(*pToken - '0');
                ++pToken;
            }
        }

        // Now process the token:
        if (*pToken == ')')
            pToken++;
        else
            while (*pToken != ' ')
                ++pToken;

        // If this is a value, push it onto the stack:
        if (v > 0)
            valueStack.push(v);

        // If this is an operator, pop two operands and apply the operation:
        if (*pToken == '+' || *pToken == '-' ||
            *pToken == '*' || *pToken == '/' ||
            *pToken == '^') {
            int op = *pToken;
            long long b = valueStack.top();
            valueStack.pop();
            long long a = valueStack.top();
            valueStack.pop();

            switch (op) {
                case '+':
                    v = a + b;
                    break;
                case '-':
                    v = a - b;
                    break;
                case '*':
                    v = a * b;
                    break;
                case '/':
                    if (b == 0)
                        return LONG_LONG_MAX; // invalid operation
                    v = a / b;
                    break;
                case '^':
                    v = pow(a, b);
                    break;
            }

            valueStack.push(v);
        }
    }

    return valueStack.top();
}

long long pow(long long a, long long b) {
    if (b == 0)
        return 1;
    else
        return a * pow(a, b - 1);
}