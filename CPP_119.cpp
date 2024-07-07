#include <iostream>
#include <vector>
using namespace std;

bool match_parens(vector<string> lst) {
    int countOpen = 0;
    int countClose = 0;

    for (const string& s : lst) {
        for (char c : s) {
            if (c == '(') {
                countOpen++;
            } else if (c == ')') {
                countClose++;
            }
        }
    }

    if (countOpen == countClose) {
        return true;
    } else {
        return false;
    }
}

int main() {
    vector<string> lst = {")", "("};
    assert(match_parens(lst));
    return 0;
}