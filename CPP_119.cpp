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

    vector<string> lst = {"(abc)", "def(", "(ghi)"};
    int result = match_parens(lst);
    cout << (result == 1 ? "Yes" : "No") << endl;

    return 0;
}