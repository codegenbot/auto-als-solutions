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

    std::string input_map_str = argv[1];
    map<string, string> dict;
    // parse the input map from the command line argument...
    
    if (std::ifstream(input_map_str)) {
        std::ifstream file(input_map_str);
        std::string key, value;
        while (file >> key >> value) {
            dict[key] = value;
        }
    } else {
        std::cerr << "Error opening file: " << input_map_str << std::endl;
        return 1;
    }

    assert(check_dict_case(dict) == true);

    return 0;
}