#include <string>
#include <map>
#include <cctype>

bool check_map_case(map<string, string> pair) {
    bool all_lower = true;
    bool all_upper = true;

    for (auto& key_value : pair) {
        if (pair.empty()) {
            return false;
        }
        string key = key_value.first;
        if (!(islower(key[0]) || isupper(key[0]))) {
            return false;
        }
        if (!all_lower) all_upper = true;
        if (!all_upper) all_lower = true;
    }

    return all_lower || all_upper;
}