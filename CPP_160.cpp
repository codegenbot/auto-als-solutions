#include <vector>
#include <cmath>

int do_algebra(vector<pair<char, int>> expressions) {
    int result = 0;
    for (auto& expression : expressions) {
        char operator_;
        int operand;
        std::tie(operator_, operand) = expression;

        if (operator_ == '+') {
            result += operand;
        } else if (operator_ == '-') {
            result -= operand;
        } else if (operator_ == '*') {
            int temp = 1;
            for (int i = 0; i < expressions.size(); i++) {
                if (expressions[i].first == '*')
                    temp *= expressions[i].second;
            }
            result += temp * operand;
        } else if (operator_ == '/') {
            int temp = 1;
            for (int i = 0; i < expressions.size(); i++) {
                if (expressions[i].first == '/')
                    temp /= expressions[i].second;
            }
            result += temp / operand;
        } else if (operator_ == '**') {
            int temp = 1;
            for (int i = 0; i < expressions.size(); i++) {
                if (expressions[i].first == '**')
                    temp *= pow(expressions[i].second, 1);
            }
            result += temp * pow(operand, 1);
        }
    }
    return result;
}