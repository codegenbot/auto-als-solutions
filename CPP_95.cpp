#include <iostream>
#include <map>
#include <string>

using namespace std;

bool check_dict_case(map<basic_string<char>, basic_string<char>> dict) {
    if(dict.empty()) return false;
    
    bool allLower = true;
    bool allUpper = true;
    
    for(auto& pair : dict) {
        basic_string<char> key = pair.first;
        if(!allLower && !allUpper) break;
        if(allLower && !islower(key[0])) allLower = false;
        if(allUpper && !isupper(key[0])) allUpper = false;
    }
    
    return allLower || allUpper;
}

int main() {
    map<basic_string<char>, basic_string<char>> dict;
    // Add your code here to fill the dictionary
    cout << check_dict_case(dict) << endl;
    return 0;
}