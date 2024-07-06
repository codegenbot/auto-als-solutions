```cpp
#include <vector>
#include <list>
#include <boost/any.hpp>

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        boost::optional<int> oint = boost::any_cast<boost::optional<int>>(value);
        if(oint) {
            int num = boost::any_cast<int>(value);
            result.push_back(num);
        }
    }
    return result;