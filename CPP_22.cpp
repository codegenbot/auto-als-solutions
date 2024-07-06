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
    list<boost::any> values;
    values.push_back('c');
    values.push_back('a');
    values.push_back('b');

    vector<int> output = filter_integers(values);
    
    if (issame({97, 97, 98}, output)) {
        cout << "The output is same as expected." << endl;
    } else {
        cout << "The output is not same as expected." << endl;
    }
    
    return 0;
}