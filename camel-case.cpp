#include <string>
using namespace std;

string camelCase(string s) {
    string result;
    int i = 0;
    
    while (i < s.length()) {
        if (s[i] == '-') {
            i++; // skip '-'
            while (i < s.length() && s[i] == '-') i++; // skip multiple '-'
            char first = toupper(s[i]);
            result += first; // capitalize the next word
            i++; // skip the first character of the next word
        } else if (s[i] == ' ') {
            while (i < s.length() && s[i] == ' ') i++; // skip multiple spaces
            char first = tolower(s[i]);
            result += first; // lowercase the next word
            i++; // skip the first character of the next word
        } else {
            char c = tolower(s[i]);
            result += c;
            i++;
        }
    }
    
    return result;
}

int main() {
    int t;
    cin >> t;
    while(t--) {
        string s;
        cin >> s;
        cout << camelCase(s) << endl;
    }
    return 0;
}