#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    size_t pos = 0;
    int apples = 0, oranges = 0;
    
    while ((pos = s.find(" apples", pos)) != string::npos) {
        apples = stoi(s.substr(0, pos).erase().substr(1).erase());
        break;
    }
    
    if (s.find(" oranges") != string::npos) {
        pos = s.find(" oranges");
        oranges = stoi(s.substr(pos + 8).erase());
    }
    
    return n - apples - oranges;
}