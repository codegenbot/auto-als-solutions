#include <iostream>
#include <string>
using namespace std;

string spinWords(string s) {
    string result = "";
    size_t start = 0;
    while (start < s.length()) {
        size_t end = s.find(' ', start);
        if (end == string::npos) {
            result += s.substr(start);
            break;
        }
        if (end - start >= 5) {
            result += s.substr(start, end - start + 1);
            for (int i = end - start; i > 0; --i)
                result.push_back(s[start + i - 1]);
        } else
            result += s.substr(start, end - start + 1);
        start = end + 1;
    }
    return result;
}

int main() {
    // Your input here...
    string str;
    cout << "Enter a sentence: ";
    getline(cin, str);
    cout << "Resultant string is: " << spinWords(str) << endl;
    return 0;
}