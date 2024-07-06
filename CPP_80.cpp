```c++
#include <iostream>
#include <string>
using namespace std;

bool is_happy(string s) {
    if(s.length() < 3) return false;
    for(int i = 0; i <= s.length()-3; i++){
        string str = s.substr(i, 3);
        bool unique = true;
        for(char c : str){
            int count = 0;
            for(int j = i; j <= i+2; j++){
                if(s[j] == c) count++;
            }
            if(count > 1) {
                unique = false;
                break;
            }
        }
        if(!unique) return false;
    }
    return true;
}

int main() {
    string s;
    cout << "Enter a string: ";
    cin >> s;
    if(is_happy(s)) {
        cout << "The string is happy." << endl;
    } else {
        cout << "The string is not happy." << endl;
    }
    return 0;
}