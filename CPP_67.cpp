#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    int total = 0;
    string temp;
    for(int i=0; i<s.length(); i++) {
        if(s[i] == ' ') {
            continue;
        }
        if(!isdigit(s[i])) {
            break;
        }
        temp += s[i];
    }
    int apples = stoi(temp);
    total += apples;

    temp = "";
    for(int i=s.length()-1; i>=0; i--) {
        if(s[i] == ' ') {
            continue;
        }
        if(!isdigit(s[i])) {
            break;
        }
        temp += s[i];
    }
    reverse(temp.begin(), temp.end());
    int oranges = stoi(temp);
    total += oranges;

    return n - apples - oranges;
}