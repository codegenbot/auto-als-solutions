#include <any>
#include <vector>
#include <list>

namespace std;

typedef any Any;
typedef optional<int> OInt;

vector<int> filter_integers(list<Any> values) {
    vector<int> result;
    for (const auto& value : values) {
        OInt oint = get_if<OInt>(&value);
        if(oint) {
            result.push_back(get<OInt>(value));
        }
    }
    return result;