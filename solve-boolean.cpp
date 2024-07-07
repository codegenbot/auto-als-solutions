#include <vector>
#include <iostream>
using namespace std;

bool solveBoolean(string s) {
    if (s == "T" || s == "t")
        return true;
    else if (s == "F" || s == "f")
        return false;
    else if (s.length() > 1 && s[0] == 'n' && s[1] == '&') {
        return !solveBoolean(string(s, 2));
    } else if (s.length() > 1 && s[0] == '|') {
        return solveBoolean(string(s, 1)) || solveBoolean(string(s, 2));
    } else
        return false;
}

int main() {
    string s;
    cin >> s;
    cout << boolalpha << solveBoolean(s) << endl;
    return 0;
}