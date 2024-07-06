#include <string>
#include <map>
#include <cctype>

bool check_dict_case(std::map<std::string, std::string> dict) {
    for (auto &pair : dict) {
        if (!pair.first.empty() && 
            (!std::isupper(pair.first[0]) || !std::islower(pair.first))) 
            return false;
    }
    return true;
}

int main() {
    std::map<std::string, std::string> myDict;
    // ... populate the dictionary ...
    assert(check_dict_case(myDict) == true);
    return 0;
}