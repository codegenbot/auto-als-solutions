```
#include <vector>
#include <list>
#include <optional>
#include <typeindex>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    return a.size() == b.size() && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<int> filter_integers(std::list<std::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(int)) {
            try {
                int num = std::any_cast<int>(value);
                result.push_back(num);
            } catch(const std::bad_any_cast&) {
                // Ignore non-integer values
            }
        }
    }
    return result;
}

int main() {
    assert(issame(filter_integers({3, 4, 3, 3, 1, 'a', 'b'}), {3, 3, 3}));
    return 0;
}