#include <string>
using namespace std;

bool solveBoolean(string s) {
    stack<char> st;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '|') {
            while (!st.empty()) st.pop();
        } else if (s[i] == '&') {
            while (st.size() > 1) st.pop();
        } else if (s[i] == 't' || s[i] == 'f') {
            st.push(s[i]);
        }
    }
    return st.top() == 't';
}

int main() {
    string input;
    cout << "Enter a Boolean expression: ";
    cin >> input;
    bool result = solveBoolean(input);
    if (result) cout << "True" << endl;
    else cout << "False" << endl;
    return 0;
}