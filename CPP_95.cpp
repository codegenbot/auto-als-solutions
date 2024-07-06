#include <map>
#include <string>
#include <algorithm>

bool check_dict_case(std::map<std::string, std::string> dict){
    if(dict.empty()) return false;
    bool allLower = true;
    bool allUpper = true;

    for(auto& pair : dict) {
        string key = pair.first;
        if(!allLower && !allUpper) break;
        if(allLower && !std::all_of(key.begin(), key.end(), ::islower)) allLower = false;
        if(allUpper && !std::all_of(key.begin(), key.end(), ::isupper)) allUpper = false;
    }

    return allLower || allUpper;
}

int main() {
    std::map<std::string, std::string> dict;
    // Add elements to the dictionary here
    std::cout << check_dict_case(dict) << std::endl; 
    return 0;
}