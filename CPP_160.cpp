#include <vector>
#include <cmath>

int do_algebra(vector<pair<char, int>> expressions) {
    int result = 0;
    for (auto& expression : expressions) {
        if (expression.first == '+') {
            result += expression.second;
        } else if (expression.first == '-') {
            result -= expression.second;
        } else if (expression.first == '*') {
            int temp = expression.second;
            for (int i = 1; i < expressions.size(); i++) {
                temp *= expressions[i].second;
            }
            result += temp;
        } else if (expression.first == '/') {
            int temp = expression.second;
            for (int i = 1; i < expressions.size(); i++) {
                temp /= expressions[i].second;
            }
            result += temp;
        } else if (expression.first == '^') {
            int temp = 1;
            for (int i = 0; i < expressions.size(); i++) {
                temp *= pow(expressions[i].second, 1);
            }
            result += temp;
        }
    }
    return result;
}