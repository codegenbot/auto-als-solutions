#include <iostream>
using namespace std;

string change_base(int x, int base) {
    string s = "";
    while (x > 0) {
        int rem = x % base;
        if(rem < 10)
            s.push_back('0' + rem);
        else if(rem <= 35)
            s.push_back('A' + rem - 10);
        else
            s.push_back('-');
        x /= base;
    }
    return string reversal(s);
}

string reversal(string str) {
    int n = str.length();
    for(int i=n-1; i>=0; i--) {
        cout << str[i];
    }
}