#include <optional>
#include <vector>
#include <list>

std::vector<int> filter_integers(std::list<any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(Optional<int>)) {
            try {
                Optional<int> oint = any_cast<Optional<int>>(value);
                if (oint.has_value()) {
                    result.push_back(oint.value());
                }
            } catch (bad_any_cast&) {
                // Ignore non-Optional values
            }
        }
    }
    return result;
}