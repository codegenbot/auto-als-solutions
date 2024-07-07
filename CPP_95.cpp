```cpp
#include <map>
#include <string>
#include <cctype>

bool check_dict_case(std::map<std::string, std::string> dict) {
    if (dict.empty()) return false;
    bool allLower = true, allUpper = true;
    for (auto& pair : dict) {
        if (!allLower && !allUpper) break;
        if (!islower(pair.first[0])) allLower = false;
        if (!isupper(pair.first[0])) allUpper = false;
    }
    return allLower || allUpper;
}

int main() {
    assert(check_dict_case({}) == false);
    return 0;
}