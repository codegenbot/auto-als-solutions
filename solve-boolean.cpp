#include <vector>
#include <iostream>
#include <string>

using namespace std;

bool solveBoolean(string input) {
    bool result = (input == "t") || (input == "T");
    
    if (result) {
        for (int i = 1; i < input.length(); i++) {
            if (input[i] == '&') {
                return false;
            } else if (input[i] == '|') {
                result = false;
                break;
            }
        }
        
        if (!result && input[input.length() - 1] == '&') {
            result = true;
        }
    } else {
        for (int i = 1; i < input.length(); i++) {
            if (input[i] == '|') {
                return false;
            } else if (input[i] == '&') {
                result = true;
                break;
            }
        }
        
        if (!result && input[input.length() - 1] == '|') {
            result = true;
        }
    }
    
    return result;
}

int main() {
    // Your code goes here
    string s;
    cout << "Enter the boolean expression: ";
    cin >> s;
    bool output = solveBoolean(s);
    if (output)
        cout << "True";
    else
        cout << "False";
    return 0;
}