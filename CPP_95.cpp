#include <string>
#include <map>
#include <cctype>

bool check_dict_case(std::map<std::string, std::string> dict) {
    for (const auto &pair : dict) {
        if (!pair.first.empty() && !isupper(pair.first[0]) && !islower(pair.first[0])) 
            return false;
    }
    return true;
}

int main() {
    std::map<std::string, std::string> myDict;
    // ... populate the dictionary ...
    assert(check_dict_case(myDict) == false);
    return 0;
}