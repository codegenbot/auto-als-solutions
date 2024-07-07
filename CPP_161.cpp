#include <string>

string solve(string s){
    string result = "";
    for(int i=0; i<s.length();i++){
        if(isalpha(s[i])){
            if(islower(s[i]))
                result += toupper(s[i]);
            else
                result += tolower(s[i]);
        }
        else
            result += s[i];
    }
    if(result.empty())
        return string(1, result[0]).append(string(result.length()-1, char(result[0])));
    return result;
}