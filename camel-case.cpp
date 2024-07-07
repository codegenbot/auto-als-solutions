#include <iostream>
#include <string>
using namespace std;

string camelCase(string s) {
    string result = "";
    int flag = 1;
    
    for(int i=0; i<s.length(); i++) {
        if(s[i] == '-') {
            if(flag) {
                flag = 0;
                continue;
            } else {
                result += s[i+1].toupper();
                i++;
            }
        } 
        if(flag) {
            result += s[i];
        } else {
            result += s[i].tolower();
            flag = 1;
        }
    }
    
    return result;
}

int main() {
    string str;
    cout << "Enter the kebab-case string: ";
    cin >> str;
    cout << "The camelCase is: " << camelCase(str) << endl;
    return 0;
}