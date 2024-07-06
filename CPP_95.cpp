#include <string>
#include <map>
#include <cctype>

bool check_map_case(std::map<std::string, std::string> dict) {
    bool all_lower = true;
    bool all_upper = true;

    for (auto& pair : dict) {
        if (pair.first.empty()) {
            return false;
        }
        string key = pair.first;
        if (!islower(key[0]) && !isupper(key[0])) {
            return false;
        }
        if (!all_lower) all_upper = true;
        if (!all_upper) all_lower = true;
    }

    return all_lower || all_upper;
}