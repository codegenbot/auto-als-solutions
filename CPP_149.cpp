#include <vector>
#include <algorithm>
#include <string>

bool issame(const std::vector<std::string>& a, const std::vector<std::string>& b) {
    if (a.size() != b.size())
        return false;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            return false;
    }

    return true;
}

std::vector<std::string> sorted_list_sum(const std::vector<std::string>& lst) {
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
    assert(issame(sorted_list_sum(vec1), vec2));
    return 0;
}