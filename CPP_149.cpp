```
#include <vector>
#include <algorithm>
#include <string>
#include <pmr/string>

bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    if (a.size() != b.size())
        return false;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            return false;
    }

    return true;
}

std::vector<std::pmr::string> sortedListSum(std::vector<std::string> lst) {
    std::vector<std::pmr::string> result;
    for (const auto& str : lst) {
        if (std::stoi(str) % 2 == 0) {
            result.push_back(str);
        }
    }
    std::sort(result.begin(), result.end(),
        [&](const std::pmr::string& a, const std::pmr::string& b) {
            if (std::stoi(a) != std::stoi(b)) {
                return std::stoi(a) < std::stoi(b);
            } else {
                return a < b;
            }
        });
    return result;
}