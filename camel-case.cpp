#include <vector>
#include <iostream>
#include <string>

std::string camelCase(const std::string& input) {
    std::string output;
    bool first = true;

    for (char c : input) {
        if (c == '-') {
            continue;
        }
        if (!first) {
            output[0] = toupper(output[0]);
        } else {
            first = false;
        }
        output += c;
    }

    return output;
}

int main() {
    std::string input;
    std::cin >> input;
    std::cout << camelCase(input) << std::endl;

    return 0;
}