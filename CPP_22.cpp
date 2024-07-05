#include <optional>
#include <vector>
#include <list>

using namespace std;

vector<int> filter_integers(list<any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (any_cast<optional<int>>(value)) {
            result.push_back(any_cast<int>(value));
        }
    }
    return result;
}