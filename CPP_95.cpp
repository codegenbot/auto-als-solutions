#include <iostream>
#include <string>
#include <map>

bool check_dict_case(map<string,string> dict){ 
    if(dict.empty()) return false;
    bool allLower = true;
    bool allUpper = true;
    
    for(auto& pair : dict) {
        string key = pair.first;
        if(!allLower && !allUpper) break;
        if(allLower && !islower(key[0])) allLower = false;
        if(allUpper && !isupper(key[0])) allUpper = false;
    }
    
    return allLower || allUpper;
}

int main() {
    assert(check_dict_case({}) == false);
    return 0;
}