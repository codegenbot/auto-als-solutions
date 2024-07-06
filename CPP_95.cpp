#include <iostream>
#include <map>
#include <cctype>

bool check_dict_case(std::map<std::string, std::string> dict) {
    if (dict.empty()) return false;

    bool allLower = true;
    bool allUpper = true;

    for (auto& pair : dict) {
        if (!islower(pair.first[0])) allLower = false;
        if (!isupper(pair.first[0])) allUpper = false;
    }

    return allLower || allUpper;
}

int main() {
    std::map<std::string, std::string> dict;
    // Add code to read input from the user and store it in the dictionary
    // Then call check_dict_case(dict) and print the result

    return 0;
}