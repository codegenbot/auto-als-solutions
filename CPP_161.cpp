```cpp
#include <iostream>
#include <string>
using namespace std;

string solve(string s){
    string result = "";
    for(int i=0; i<s.length(); i++){
        if(isalpha(s[i])){
            result += (s[i] >= 'a' && s[i] <= 'z') ? toupper(s[i]) : tolower(s[i]);
        }else{
            result += s[i];
        }
    }
    return result;
}

int main(){
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    cout << solve(str) << endl;
    return 0;
}