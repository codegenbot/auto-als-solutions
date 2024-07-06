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
                OInt oint = boost::any_cast<OInt>(value);
                if (oint.is_initialized()) {
                    result.push_back(*oint);
                }
            } catch (boost::bad_any_cast&) {
                // Ignore non-OInt values
            }
        }
    }
    return result;
}