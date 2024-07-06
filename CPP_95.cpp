#include <cassert>
#include <map>
#include <string>
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

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cerr << "Usage: " << argv[0] << " <input_map>" << std::endl;
        return 1;
    }

    string input_map_str = argv[1];
    map<string, string> dict;
    // parse the input map from the command line argument...
    int pos = input_map_str.find(',');
    while (pos != string::npos) {
        size_t eq_pos = input_map_str.find('=');
        if (eq_pos == string::npos || pos > eq_pos)
            break;
        string key = input_map_str.substr(0, eq_pos);
        string value = input_map_str.substr(eq_pos + 1, pos - (eq_pos + 1));
        dict.insert({key, value});
        input_map_str.erase(0, pos + 1);
        pos = input_map_str.find(',');
    }

    assert(check_dict_case(dict) == true);

    return 0;
}