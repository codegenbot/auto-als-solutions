#include <iostream>
#include <string>

using namespace std;

bool is_palindrome(string str) {
    string s(str.rbegin(),str.rend());
    return s==str;
}

string make_palindrome(string str){
    int i=str.length()-1;
    while(i>=0 && str[i]==str[0])
        i--;
    if(i<0)
        return str+str;
    return str.substr(0,i+1)+str.substr(i+1, str.length()-i-1).reverse();
}

int main() {
    string s;
    cout<<"Enter a string: ";
    cin>>s;
    cout << "The shortest palindrome that begins with the supplied string is: "<<make_palindrome(s)<<endl;
    return 0;
}