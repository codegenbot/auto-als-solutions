```cpp
#include <boost/any.hpp>
#include <boost/optional.hpp>
#include <vector>
#include <list>

namespace boost {
    using namespace std;
}

typedef boost::optional<int> OInt;

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(OInt)) {
            OInt oi = boost::any_cast<OInt>(value);
            if (oi) {
                result.push_back(*oi);
            }
        }
    }
    return result;
}