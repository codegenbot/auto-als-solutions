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
        if(auto opt = boost::any_cast<OInt>(value)) {
            result.push_back(opt.get());
        }
    }
    return result;
}