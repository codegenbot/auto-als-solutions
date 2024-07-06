#include <boost/any.hpp>
#include <vector>
#include <list>

namespace boost {
    using namespace std;
}

typedef boost::any Any;
typedef boost::optional<int> OInt;

vector<int> filter_integers(list<Any> values) {
    vector<int> result;
    for (const auto& value : values) {
        OInt oint = boost::any_cast<OInt>(value);
        if(oint) {
            int num = boost::any_cast<int>(value);
            result.push_back(num);
        }
    }
    return result;
}