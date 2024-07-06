#include <map>
#include <string>

int main() {
    std::map<std::string, std::string> dict;
    std::cout << "Enter key-value pairs (separated by space) and press Enter to stop: \n";
    for(std::string line; getline(std::cin, line); ) {
        size_t sep = line.find(' ');
        if(sep != std::string::npos) {
            std::string key = line.substr(0, sep);
            std::string value = line.substr(sep + 1);
            dict[key] = value;
        } else break;
    }
    
    bool result = check_dict_case(dict);
    std::cout << "Dictionary case: " << (result ? "all lower or upper" : "mixed") << "\n";
    return 0;

}

bool check_dict_case(map<string,string> dict){
    if(dict.empty()) return false;
    bool allLower = true;
    bool allUpper = true;
    
    for(auto& pair : dict) {
        std::string key = pair.first;
        if(!allLower && !allUpper) break;
        if(allLower && !islower(key[0])) allLower = false;
        if(allUpper && !isupper(key[0])) allUpper = false;
    }
    
    return allLower || allUpper;
}