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
    string input;
    cout << "Enter a string: ";
    getline(cin, input); 
    if(input.empty()){
        cout << "Error! Please enter a valid input." << endl;
    } else {
        string output = solve(input);
        cout << "Output: " << output << endl;
    }
    return 0;
}