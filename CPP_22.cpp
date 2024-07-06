```cpp
#include <vector>
#include <list>
#include <optional>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (int i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

std::vector<int> filter_integers(const std::list<std::any>& values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(std::optional<int>) && value.any_cast<std::optional<int>>().has_value()) {
            int num = value.any_cast<std::optional<int>>().value();
            result.push_back(num);
        }
    }
    return result;
}

int main() {
    std::list<std::any> values({std::optional<int>(1), std::optional<int>(2), std::optional<int>(3)});
    assert(issame(filter_integers(values), {1, 2, 3}));
    return 0;
}