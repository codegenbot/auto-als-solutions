```cpp
#include <vector>
using namespace std;

int do_alphabet(vector<pair<string, int>> expressions) {
    int result = expressions[0].second;
    for (int i = 0; i < expressions.size() - 1; i++) {
        if (expressions[i].first == "+") {
            result += expressions[i + 1].second;
        } else if (expressions[i].first == "-") {
            result -= expressions[i + 1].second;
        } else if (expressions[i].first == "*") {
            result *= expressions[i + 1].second;
        } else if (expressions[i].first == "/") { // note: floor division is not a standard operator in C++
            result /= expressions[i + 1].second; // this will perform integer division
        }
    }
    return result;
}