#include "/usr/include/boost/any.hpp"
using namespace boost;

typedef boost::any Any;
typedef boost::optional<int> OInt;

vector<int> filter_integers(list<Any> values) {
    vector<int> result;
    for (const auto& value : values) {
        OInt oint = boost::any_cast<OInt>(value);
        if(oint) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}