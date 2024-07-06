#include <boost/optional.hpp>

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(boost::optional<int>)) {
            if(value.any().is_none())
                continue;
            else
                result.push_back(boost::any_cast<boost::optional<int>>(value).get());
        }
    }
    return result;
}