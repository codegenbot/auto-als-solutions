#include <string>
#include <map>

bool check_dict_case(std::map<std::string, std::string> dict) {
    for (auto &pair : dict) {
        if (pair.first.length() > 0 && (!isupper(pair.first[0]) || !islower(pair.first))) 
            return false;
    }
    return true;
}