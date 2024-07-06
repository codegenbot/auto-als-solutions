```cpp
#include <vector>
#include <list>
#include <boost/any.hpp>

bool issame(vector<int> a, vector<int> b) {
    return a == b;
}

vector<int> filter_integers(list<boost::any> values) {
    vector<int> result;
    for (const auto& value : values) {
        if (boost::any_cast<int>(value).good()) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}

int main() {
    list<boost::any> values = {'1', '2', '3'};
    vector<int> output = filter_integers(values);
    if (issame({1, 2, 3}, output)) {
        cout << "Vectors are same";
    } else {
        cout << "Vectors are not same";
    }
    return 0;
}