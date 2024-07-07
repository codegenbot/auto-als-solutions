#include <vector>
#include <cmath>

int do_algebra(vector<pair<char, int>> expressions) {
    int result = 0;
    for (const auto& expression : expressions) {
        switch (expression.first) {
            case '+':
                result += expression.second;
                break;
            case '-':
                result -= expression.second;
                break;
            case '*':
                for (int i = expressions.size() - 1; i >= 0; --i) {
                    if (expressions[i].first == '*') {
                        result *= expressions[i].second;
                    }
                }
                break;
            case '/':
            case '//':
                int temp = expression.second;
                for (int i = expressions.size() - 1; i >= 0; --i) {
                    if ((expressions[i].first == '/') || (expressions[i].first == '//')) {
                        temp /= expressions[i].second;
                    }
                }
                result = temp;
                break;
            case '^':
                int temp2 = 1;
                for (int i = expressions.size() - 1; i >= 0; --i) {
                    if (expressions[i].first == '^') {
                        temp2 = pow(temp2, expressions[i].second);
                    }
                }
                result = temp2;
                break;
        }
    }
    return result;
}