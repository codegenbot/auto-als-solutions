#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a, std::string b) {
    if (a.size() != 1 || a[0] != b)
        return false;

    for (int i = 1; i < a.size(); i++) {
        if (a[i] != b)
            return false;
    }

    return true;
}

std::vector<std::string> sortedListSum(std::vector<std::string> lst) {
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

int main(int argc, char** argv) {
    std::vector<std::string> vec1 = {"aaaa", "bbbb", "dd", "cc"};
    std::vector<std::string> vec2 = {"cc", "dd", "aaaa", "bbbb"};
    assert(issame(sortedListSum(vec1), (std::string)vec2));
    return 0;
}