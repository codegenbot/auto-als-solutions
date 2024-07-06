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
            try {
                int num = boost::any_cast<OInt>(value).get();
                result.push_back(num);
            } catch(boost::bad_any_cast const&) {
                // Ignore non-integer values
            }
        }
    }
    return result;
}