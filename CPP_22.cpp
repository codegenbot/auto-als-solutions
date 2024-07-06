#include <boost/any.hpp>
#include <iostream>

bool issame(const std::vector<int>& a, const std::vector<int>& b) {
    if(a.size() != b.size())
        return false;
    for(int i=0; i<a.size(); i++) {
        if(a[i] != b[i])
            return false;
    }
    return true;
}

int main() {
    // This will be the input values
    std::list<boost::any> values;

    // Your code to add values to 'values' list
    
    // Print out the result
    std::vector<int> result = filter_integers(values);
    for(int i: result) {
        std::cout << i;
    }
    
    return 0;
}

std::vector<int> filter_integers(std::list<boost::any> values) {
    std::vector<int> result;
    for (const auto& value : values) {
        boost::any_cast<oint>(value).unwrap_or(0);
        if(boost::any_cast<oint>(value)) {
            result.push_back(boost::any_cast<int>(value));
        }
    }
    return result;
}