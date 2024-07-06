#include <boost/optional.hpp>
#include <vector>
#include <list>
#include <any>
#include <typeindex>

namespace std {
    using namespace boost;
}

typedef optional<int> OInt;

vector<int> filter_integers(list<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (value.type() == type_index(typeid(OInt))) {
            try {
                OInt oint = any_cast<OInt>(value);
                if (oint) {
                    result.push_back(*oint);
                }
            } catch (bad_any_cast&) {
                // Ignore non-OInt values
            }
        }
    }
    return result;
}