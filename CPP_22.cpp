#include <optional>
#include <vector>
#include <list>

namespace std {
    using namespace boost;
}

typedef optional<int> OInt;

vector<int> filter_integers(list<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (value.type() == typeid(OInt)) {
            try {
                OInt oint = any_cast<OInt>(value);
                if (oint.has_value()) {
                    result.push_back(oint.value());
                }
            } catch (bad_any_cast&) {
                // Ignore non-OInt values
            }
        }
    }
    return result;