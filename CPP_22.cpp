```cpp
#include <boost/optional.hpp>

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(boost::optional<int>)) {
            boost::optional<int> opt = boost::any_cast<boost::optional<int>>(value);
            if (opt) {
                result.push_back(*opt);
            }
        }
    }
    return result;
}