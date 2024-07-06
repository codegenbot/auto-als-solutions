```cpp
#include <vector>
#include <list>
#include <optional>
#include <type_traits>

std::vector<int> filter_integers(const std::list<std::any>& values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(std::optional<int})) {
            try {
                int num = std::any_cast<std::optional<int>>(value).value();
                result.push_back(num);
            } catch (...) {
                // Ignore non-integer values
            }
        }
    }
    return result;
}

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if (a.size() != b.size()) {
        return false;
    }
    for (size_t i = 0; i < a.size(); ++i) {
        if (a[i] != b[i]) {
            return false;
        }
    }
    return true;
}

int main() {
    assert(issame({1, 2, 3}, {1, 2, 3}));
    return 0;
}