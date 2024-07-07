#include <vector>
#include <cmath>

int do_algebra(vector<pair<char, int>> expressions) {
    int result = 0;
    for (const auto& expression : expressions) {
        char operator_;
        int operand_;
        std::tie(operator_, operand_) = expression;

        if (operator_ == '+') {
            result += operand_;
        } else if (operator_ == '-') {
            result -= operand_;
        } else if (operator_ == '*') {
            int temp = 1;
            for (int i = 0; i < operand_; ++i) {
                temp *= expressions[i].second;
            }
            result += temp;
        } else if (operator_ == '/') {
            int temp = expressions[operand_ - 1].second;
            for (int i = operand_ + 1; i < expressions.size(); ++i) {
                temp /= expressions[i].second;
            }
            result += temp;
        } else if (operator_ == '^') {
            int temp = 1;
            for (int i = 0; i < operand_; ++i) {
                temp *= pow(expressions[i].second, 1);
            }
            result += temp;
        }
    }
    return result;
}