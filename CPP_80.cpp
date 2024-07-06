```cpp
#include <iostream>
#include <string>
#include <map>

using namespace std;

bool is_happy(string s){
    if(s.length() < 3) return false;
    for(int i = 0; i <= s.length()-3; i++){
        string str = s.substr(i, 3);
        map<char, int> freqMap;
        bool unique = true;
        for(char c : str){
            if(freqMap[c]++) {
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
    getline(cin, s);
    if(is_happy(s))
        cout << "The given string is happy." << endl;
    else
        cout << "The given string is not happy." << endl;
    return 0;
}