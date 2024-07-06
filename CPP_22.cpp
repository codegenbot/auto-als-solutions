#include <vector>
#include <list>
#include <boost/any.hpp>

bool issame(std::vector<int> a, std::vector<int> b) {
    return a == b;
}

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (boost::any_cast<int>(value).good()) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}

int main() {
    std::list<boost::any> values;
    values.push_back('c');
    values.push_back('a');
    values.push_back('b');

    std::vector<int> output = filter_integers(values);
    if (issame({97, 97, 98}, output)) {
        return 0;
    } else {
        return 1;
    }
}