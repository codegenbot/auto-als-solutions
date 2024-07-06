#include <string>
#include <iostream>

std::string solve(std::string input) {
    int count = 0;
    for (char c : input) {
        if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u') {
            count++;
        }
    }
    return std::to_string(count);
}