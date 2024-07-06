#include<string>
using namespace std;

bool is_palindrome(string str){
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    int i = 0; // pointer for prefix
    int j = str.length() - 1; // pointer for suffix

    while(i <= j && str[i] == str[j]){
        i++;
        j--;
    }

    string palindrome;
    palindrome += str.substr(0, i); // add the non-palindromic part to the palindrome
    string rev = str.substr(i); // reverse the remaining part
    reverse(rev.begin(), rev.end()); // make it a palindrome
    palindrome += rev; // add the reversed part to the palindrome

    return palindrome;
}