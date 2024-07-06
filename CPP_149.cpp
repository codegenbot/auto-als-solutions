```cpp
#include <vector>
#include <algorithm>
#include <string>

bool same(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    if (a.size() != b.size())
        return false;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            return false;
    }

    return true;
}

std::vector<std::string> sortedListSum(std::vector<std::string> lst) {
    std::vector<std::string> result;
    for (const auto& str : lst) {
        if (stoi(str) % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(),
        [&](const std::string& a, const std::string& b) {
            if (stoi(a) != stoi(b)) {
                return stoi(a) < stoi(b);
            } else {
                return a < b;
            }
        });
    return result;
}

int main() {
    std::vector<std::string> vec1 = {"aaaa", "bbbb", "dd", "cc"};
    std::vector<std::string> vec2 = {"cc", "dd", "aaaa", "bbbb"};
    std::vector<std::string> expected = sortedListSum(vec1);
    if (!same(expected, vec2)) {
        return 1;
    }
    return 0;
}