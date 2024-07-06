#include<string>
using namespace std;

string solve(string s){
    string result = "";
    for(char c: s){
        if(isalpha(c)){
            result += (isupper(c))? tolower(c) : toupper(c);
        } else {
            result += c;
        }
    }
    
    if(result.length() == 0) return string(reverse(s));
    return result;
}