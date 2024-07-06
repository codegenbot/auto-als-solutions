#include<string>
using namespace std;

string flip_case(string str){
    string result = "";
    for(int i=0; i<str.length();i++){
        char c = str[i];
        if(c >= 'a' && c <= 'z') // lowercase
            result += toupper(c);
        else if (c >= 'A' && c <= 'Z') // uppercase
            result += tolower(c);
        else // not a letter, just add it as is
            result += c;
    }
    return result;
}