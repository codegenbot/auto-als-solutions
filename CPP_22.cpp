```cpp
#include <vector>
#include <list>
#include <boost/any.hpp>

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

int main() {
    std::list<boost::any> values;
    values.push_back(boost::any('c'));
    values.push_back(boost::any('a'));
    values.push_back(boost::any('b'));

    std::vector<int> result = filter_integers(values);

    if (issame({1, 2, 3}, result)) {
        std::cout << "The vectors are the same." << std::endl;
    } else {
        std::cout << "The vectors are not the same." << std::endl;
    }

    return 0;
}

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        if (boost::any_cast<char>(value) >= 'a' && boost::any_cast<char>(value) <= 'z') {
            result.push_back(boost::any_cast<char>(value));
        }
    }
    return result;
}