```
#include <string>
#include <cctype>
#include <vector>
#include <algorithm>

int countDigits(const std::string& str) {
    int count = 0;
    for (char c : str) {
        if (std::isdigit(c)) {
            count++;
        }
    }
    return count;
}

std::string file_name_check(std::string file_name) {
    if (countDigits(file_name) > 3) {
        return "No";
    }

    size_t dotPos = file_name.rfind('.');
    if (dotPos == std::string::npos || file_name.find('.') != dotPos) {
        return "No";
    }

    std::string prefix = file_name.substr(0, dotPos);
    std::string suffix = file_name.substr(dotPos + 1);

    if (prefix.empty() || !std::isalpha(prefix[0])) {
        return "No";
    }

    std::vector<std::string> validSuffixes = {"txt", "exe", "dll"};
    if (std::find(validSuffixes.begin(), std::end(validSuffixes), suffix) == std::end(validSuffixes)) {
        return "No";
    }

    return "Yes";
}