Here is the completed code:

```cpp
#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return max(a.convert_to<int>(), b.convert_to<double>());
    }
    else if (a.type() == typeid(double) && b.type() == typeid(int)) {
        return max(a, boost::any(b.convert_to<int>()));
    }
    else if (a.type() == typeid(string) && b.type() == typeid(double)) {
        return (boost::any(max((stoi(get<string>(a)).convert_to<double>(), b.convert_to<double>()))));
    }
    else if (a.type() == typeid(double) && b.type() == typeid(string)) {
        return (boost::any(max(a, boost::any(stoi(get<string>(b))))));
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        if (get<string>(a) > get<string>(b))
            return a;
        else if (get<string>(a) < get<string>(b))
            return b;
        else
            return boost::any("None");
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        if (stoi(get<string>(b)) > a.convert_to<int>())
            return boost::any(stoi(get<string>(b)));
        else if (stoi(get<string>(b)) < a)
            return a;
        else
            return boost::any("None");
    }
    else if (a.type() == typeid(string) && b.type() == typeid(int)) {
        if (stoi(get<string>(a)) > b.convert_to<int>())
            return a;
        else if (stoi(get<string>(a)) < b)
            return boost::any(b);
        else
            return boost::any("None");
    }
    return boost::any("None");
}