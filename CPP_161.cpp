#include <iostream>
#include <string>
#include <cctype>

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
    string input;
    cout << "Enter a string: ";
    getline(cin, input);
    
    if(input.empty()){
        cout << "Error! You must enter a valid string." << endl;
    } else {
        string output = solve(input);
        cout << "Output: " << output << endl;
    }
    return 0;