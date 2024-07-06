```cpp
#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a) {
    if (a.size() == 0)
        return true;

    for (int i = 1; i < a.size(); i++) {
        if (!issame(std::vector<std::string>(a.begin(), a.begin() + i), std::vector<std::string>(a.begin() + i, a.end())))
            return false;
    }

    return true;
}

std::vector<std::string> sorted_list_sum(std::vector<std::string> lst) {
    std::vector<std::string> result;
    for (const auto& str : lst) {
        if (std::stoi(str) % 2 == 0) {
            result.push_back(str);
        }
    }
    std::sort(result.begin(), result.end(),
         [&](const std::string& a, const std::string& b) {
             if (std::stoi(a) != std::stoi(b)) {
                 return std::stoi(a) < std::stoi(b);
             } else {
                 return a < b;
             }
         });
    return result;
}

int main() {
    std::vector<std::string> vec1 = {"aaaa", "bbbb", "dd", "cc"};
    std::vector<std::string> vec2 = {"cc", "dd", "aaaa", "bbbb"};
    assert(issame(sorted_list_sum(vec1)) && issame(sorted_list_sum(vec2)));
    return 0;
}