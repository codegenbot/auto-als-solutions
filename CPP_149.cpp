#include <vector>
#include <algorithm>
#include <string>

bool issame(std::vector<std::string> a) {
    for (const auto& str : a) {
        if (std::stoi(str) % 2 != 0)
            return false;
    }
    return true;
}

int main() {
    std::vector<std::string> vec1 = {"aaaa", "bbbb", "dd", "cc"};
    bool same = issame(vec1);
    std::vector<std::string> vec2 = {"cc", "dd", "aaaa", "bbbb"};
    if (same) {
        for (const auto& str : vec1) {
            vec1.erase(std::remove(vec1.begin(), vec1.end(), str), vec1.end());
        }
        std::sort(vec1.begin(), vec1.end());
        assert(std::equal(vec1.begin(), vec1.end(), vec2.begin()));
    }
    return 0;
}