#include <string>
using namespace std;

string camelCase(string s) {
    string result = "";
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '-') {
            i++;
            while (i < s.length() && s[i] != ' ') {
                result += toupper(s[i]);
                i++;
            }
            result += " ";
        } else if (s[i] == ' ') {
            continue;
        } else {
            result += tolower(s[i]);
        }
    }
    return result.substr(0, 1) + result.substr(1).erase(0, 1);
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        cout << camelCase(s) << endl;
    }
    return 0;
}