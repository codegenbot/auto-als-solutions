```cpp
#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        string s = b.cast<string>();
        int num = stoi(s.erase(0,1).erase(s.length()-2,s.length()).c_str());
        return num > boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return boost::any_cast<float>(b) > boost::any_cast<float>(a) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return a.cast<string>().compare(b.cast<string>()) > 0 ? a : boost::any("None");
    }
    else {
        return boost::any("None");
    }
}

int main() {
    using namespace std;
    // use compare_one function here
}