#include <boost/optional.hpp>

namespace boost {
    using namespace std;
}

typedef boost::optional<int> OInt;

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(OInt)) {
            result.push_back(boost::any_cast<OInt>(value).get());
        }
    }
    return result;
}