#include <vector>
#include <cmath>

int do_algebra(vector<pair<char, int>> expressions) {
    int result = 0;
    for (auto &expression : expressions) {
        char operator_ = expression.first;
        int operand_ = expression.second;
        if (operator_ == '+') {
            result += operand_;
        } else if (operator_ == '-') {
            result -= operand_;
        } else if (operator_ == '*') {
            int temp = 1;
            for (int j = 0; j < operand_; j++) {
                temp *= expressions[j].second;
            }
            result += temp;
        } else if (operator_ == '/') {
            int temp = expressions[0].second / operand_;
            for (int j = 1; j < expressions.size(); j++) {
                temp /= expressions[j].second;
            }
            result += temp;
        } else if (operator_ == '**') {
            int temp = 1;
            for (int j = 0; j < operand_; j++) {
                temp *= pow(expressions[j].second, 1);
            }
            result += temp;
        }
    }
    return result;
}