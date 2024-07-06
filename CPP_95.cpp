#include <string>
#include <map>
#include <cctype>

bool check_map_case(map<string, string> pair.first) {
    bool all_lower = true;
    bool all_upper = true;

    for (auto& dict : pair.first) {
        if (dict.empty()) {
            return false;
        }
        string key = dict.first;
        if (!(islower(key[0]) || isupper(key[0]))) {
            return false;
        }
        if (!all_lower) all_upper = true;
        if (!all_upper) all_lower = true;
    }

    return all_lower || all_upper;
}