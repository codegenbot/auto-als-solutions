````
#include <iostream>
#include <string>
#include <cstring>

using namespace std;

bool is_happy(string s){
    if(s.length() < 3) return false;
    for(int i = 0; i <= s.length()-3; i++){
        char cstr[4] = {0}; 
        memcpy(cstr, s.substr(i, 3).c_str(), 3);
        bool unique = true;
        for(char d : s){ 
            if(strchr(cstr, d) != NULL) {
                unique = false;
                break;
            }
        }
        if(!unique) return false;
    }
    return true;

}

int main
{
    string s;
    cout << "Enter a string: ";
    getline(cin, s);
    if(is_happy(s))
        cout << "The given string is happy." << endl;
    else
        cout << "The given string is not happy." << endl;
    return 0;