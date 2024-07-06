#include <map>
#include <string>
#include <algorithm>

bool check_dict_case(map<string,string> dict){
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
    map<string, string> dict;
    // Add elements to the dictionary here
    cout << check_dict_case(dict) << endl; 
    return 0;
}