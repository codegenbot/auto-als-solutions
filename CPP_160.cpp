#include <vector>
int do_algebra(vector<pair<string, int>> expressions) {
    int result = expressions[0].second;
    for (int i = 1; i < expressions.size(); i++) {
        if (expressions[i].first == "+") {
            result += expressions[i].second;
        } else if (expressions[i].first == "-") {
            result -= expressions[i].second;
        } else if (expressions[i].first == "*") {
            result *= expressions[i].second;
        } else if (expressions[i].first == "/") {
            result /= expressions[i].second; // this will perform integer division
        }
    }
    return result;
}