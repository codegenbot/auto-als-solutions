#include <vector>
#include <list>
#include <optional>

bool issame(std::vector<int> a, std::vector<int> b) {
    return (a.size() == b.size()) && std::equal(a.begin(), a.end(), b.begin());
}

std::vector<int> filter_integers(std::list<std::any> values) {
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
    assert(issame(filter_integers({3, 'c', 3, 3, 'a', 'b'}), {3, 3, 3}));
    return 0;
}