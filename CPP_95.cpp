#include <map>
#include <string>
#include <assert>
#include <iostream>

bool check_dict_case(std::map<std::string, std::string> dict) {
    if (dict.empty()) return false;
    bool allLower = true;
    bool allUpper = true;

    for (auto& pair : dict) {
        std::string key = pair.first;
        if (!allLower && !allUpper) break;
        if (allLower && !islower(key[0])) allLower = false;
        if (allUpper && !isupper(key[0])) allUpper = false;
    }

    return allLower || allUpper;
}

int main() {
    std::map<std::string, std::string> dict = {{"Hello", "hello"}, {"WORLD", "world"}};
    std::cout << (check_dict_case(dict) ? "True" : "False") << std::endl;
    assert(check_dict_case(std::map<std::string, std::string>()) == false);
    return 0;
}