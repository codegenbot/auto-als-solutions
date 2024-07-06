#include <algorithm>
#include <vector>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) return false;
    for (int i = 0; i < a.size(); i++) {
        if (a[i] != b[b.size()-1-i]) return false;
    }
    return true;
}

std::vector<int> sort_array(const std::vector<int>& array) {
    std::vector<int> result(array);
    std::sort(result.begin(), result.end());
    return result;
}

int main() {
    std::vector<int> array = {21, 14, 23, 11};
    std::vector<int> result = sort_array(array);
    if (!issame(result, {23, 21, 14, 11})) {
        for (int i : result) {
            std::cout << i << " ";
        }
        return 1;
    }
    return 0;
}