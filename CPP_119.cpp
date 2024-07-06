#include <string>
#include <vector>

bool check(char c) {
    if (c == '(') return true;
    else return false;
}

bool check1(char c) {
    if (c == ')') return true;
    else return false;
}

bool match_parens(vector<string> lst) {
    int open = 0, close = 0;
    for (const string& s : lst) {
        for (char c : s) {
            if(check(c))open++;
            else if(check1(c))close++;
        }
    }
    return (open == close) ? true : false;
}

int main() {
    vector<string> input = {"(abc)", "def(", "(ghi)"};
    bool result = match_parens(input);
    cout << result << endl;
}