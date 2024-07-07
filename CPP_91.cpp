```
#include <iostream>
#include <string>
using namespace std;

int is_bored(string S) {
    int count = 0;
    string sentence;
    for (char c : S) {
        if (c == '.' || c == '?' || c == '!') {
            if (sentence.substr(0, 2) == "I am") {
                count++;
            }
            sentence = "";
        } else {
            sentence += c;
        }
    }
    return count;
}

int main() {
    string S;
    cout << "Enter a string: ";
    getline(cin, S);
    int result = is_bored(S);
    cout << "Number of boredoms: " << result << endl;
    return 0;
}