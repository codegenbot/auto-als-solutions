#include <iostream>
#include <string>
#include <vector>
using namespace std;

string match_parens(vector<string> lst) {
    int open = 0, close = 0;
    for (const string& s : lst) {
        for (char c : s) {
            if (c == '(') open++;
            else close++;
        }
    }
    return to_string(open == close);
}

int main() {
    vector<string> lst;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        lst.push_back(s);
    }
    cout << match_parens(lst) << endl;
    return 0;
}