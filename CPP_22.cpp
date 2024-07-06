```cpp
#include <optional>
#include <vector>
#include <list>

std::vector<int> filter_integers(std::list<any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (any_cast<optional<int>>(value).has_value()) {
            int num = any_cast<optional<int>>(value).get();
            result.push_back(num);
        }
    }
    return result;
}