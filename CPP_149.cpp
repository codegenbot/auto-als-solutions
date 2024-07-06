```cpp
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

bool same(std::vector<std::string> a, std::vector<std::string> b) {
    if (a.size() != b.size())
        return false;

    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[i])
            return false;
    }

    return true;
}

std::vector<std::string> sorted_list_sum(std::vector<std::string> lst) {
    std::vector<std::string> result;
    for (const auto& str : lst) {
        if (stoi(str) % 2 == 0) {
            result.push_back(str);
        }
    }
    sort(result.begin(), result.end(),
         [&](const string& a, const string& b) {
             if (stoi(a) != stoi(b)) {
                 return stoi(a) < stoi(b);
             } else {
                 return a < b;
             }
         });
    return result;
}

int main() {
    assert(same(sorted_list_sum({"aaaa", "bbbb", "dd", "cc"}), {"cc", "dd", "aaaa", "bbbb"}));
    return 0;
}