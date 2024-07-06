#include <algorithm>
#include <vector>
#include <any>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return (a.size() == b.size()) && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<int> filter_integers(const std::vector<std::any>& values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(int)) {
            int i = std::any_cast<int>(value);
            result.push_back(i);
        }
    }
    return result;
}

int main() {
    assert(issame(filter_integers({3, 12, 3, 3, 14, 'a', 'b'}), {3, 3, 3}));
    return 0;
}