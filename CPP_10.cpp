#include <algorithm>
using namespace std;

bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    if(is_palindrome(str)) return str; // If input string is palindrome, just return it

    int len = str.length();
    for(int i=len-1; i>=0; i--){
        if(!is_palindrome(str.substr(0,i)+str.substr(i))){
            return str+string(len-i-1,'a'); // Add 'a's to the end of the string
        }
    }
    return str;
}