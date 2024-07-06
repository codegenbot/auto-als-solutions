#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    int total = 0;
    string temp;
    for(int i=0; i<s.length();i++){
        if(s[i] == '1' || s[i] == '2'|| s[i] == '3'|| s[i] == '4'|| s[i] == '5'|| s[i] == '6'|| s[i] == '7'|| s[i] == '8'|| s[i] == '9'|| s[i] == '0'){
            temp += s[i];
        }else if(s[i] == 'a' || s[i] == 'A' || s[i] == 'p' || s[i] == 'P' || s[i] == 'n' || s[i] == 'N'){
            total = stoi(temp);
            temp = "";
        }
    }
    return n - total;
}