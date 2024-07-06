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
        if (value.type() == typeid(std::optional<int})) {
            try {
                int num = std::any_cast<std::optional<int>>(value).value();
                result.push_back(num);
            } catch(...) {
                // Ignore non-integer values
            }
        }
    }
    return result;
}

int main() {
    std::list<std::any> values({std::in_place_typeid<std::optional<int>>}, {1, 2, 3});
    assert(issame(filter_integers(values), {1, 2, 3}));
    return 0;
}