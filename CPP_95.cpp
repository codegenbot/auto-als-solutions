```c++
#include <map>
#include <string>
#include <cctype>

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
    map<string, string> dict = {{"A", "b"}, {"a", "B"}};
    bool result = check_dict_case(dict);
    assert(result == true);
    return 0;
}