```cpp
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
        OInt oint = boost::any_cast<OInt>(value);
        if(oint) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}