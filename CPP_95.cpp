#include <map>
#include <string>
#include <cctype>
#include <iostream>

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
    map<string, string> dict = {{"Hello", "hello"}, {"WORLD", "world"}};
    cout << (check_dict_case(dict) ? "True" : "False") << endl;
    cout << (check_dict_case(map<string, string>()) == false);
    return 0;
}