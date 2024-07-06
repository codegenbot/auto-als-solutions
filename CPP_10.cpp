#include<stdio.h>
#include<string>
using namespace std;

bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    int len = str.length();
    for(int i=len-1; i>=0; --i){
        if(!is_palindrome(str.substr(0, i+1))){
            break;
        }
    }
    string rev = str.substr(i+1);
    reverse(rev.begin(), rev.end());
    return str + rev;
}