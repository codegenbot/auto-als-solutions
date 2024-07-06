#include <stdio.h>
#include <string>
using namespace std;

int fruit_distribution(string s, int n) {
    int total_apples = 0;
    int total_oranges = 0;
    
    size_t pos = 0;
    while ((pos = s.find(" apples")) != string::npos) {
        total_apples +=stoi(s.substr(0, pos).substr(s.find(" ") + 1));
        s.erase(0, pos + " apples".size());
    }
    
    while ((pos = s.find(" oranges")) != string::npos) {
        total_oranges += stoi(s.substr(0, pos).substr(s.find(" ") + 1));
        s.erase(0, pos + " oranges".size());
    }
    
    return n - total_apples - total_oranges;
}