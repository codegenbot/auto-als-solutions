#include <boost/any.hpp>
#include <vector>
#include <list>

using boost::any_cast;
typedef long long OInt;

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if(any_cast<OInt>(value)) {
            int num = any_cast<int>(value);
            if(num != 0) {
                result.push_back(num);
            }
        }
    }
    return result;
}