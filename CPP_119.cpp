#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    string match_parens(vector<string> lst) {
        int open = 0, close = 0;
        for (const string& s : lst) {
            for (char c : s) {
                if (c == '(') open++;
                else if (c == ')') close++;
            }
        }
        return (open == close) ? 1 : 0;
    }

    int main() {
        vector<string> lst = {"(a)", "(b)", "((c))"};
        cout << match_parens(lst) << endl;
        return 0;
    }