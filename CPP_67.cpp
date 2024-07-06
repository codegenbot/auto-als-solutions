#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    int total_apples = 0;
    int total_oranges = 0;
    
    size_t pos = 0;
    while ((pos = s.find(" apples")) != string::npos) {
        total_apples += (stoi(s.substr(0, pos).erase(0, 1)) + stoi(s.substr(pos + 9)));
        break;
    }
    
    if (s.find(" oranges") != string::npos) {
        size_t pos2 = s.find(" oranges");
        total_oranges = stoi(s.substr(0, pos2).erase(0, 3));
    }
    
    return n - total_apples - total_oranges;
}