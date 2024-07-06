Here is the completed code:

```cpp
#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return max((int)a.convertible_to<int>(), (float)b.convertible_to<float>());
    }
    else if (a.type() == typeid(float) && b.type() == typeid(string)) {
        return a.convertible_to<string>() > b.convertible_to<string>() ? a : b;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return a.convertible_to<string>() > b.convertible_to<string>() ? a : (a == b ? boost::any("None") : b);
    }
    else if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return a.convertible_to<int>() > b.convertible_to<int>() ? a : ((int)a.convertible_to<int>() == (int)b.convertible_to<int>() ? boost::any("None") : b);
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return a.convertible_to<float>() > b.convertible_to<int>() ? a : ((float)a.convertible_to<float>() == (int)b.convertible_to<int>() ? boost::any("None") : b);
    }
    else if (a.type() == typeid(string) && b.type() == typeid(int)) {
        return a.convertible_to<string>() > to_string(b.convertible_to<int>()) ? a : ((a.convertible_to<string>() == to_string(b.convertible_to<int>())) ? boost::any("None") : boost::any(to_string(b.convertible_to<int>())));
    }
    else if (a.type() == typeid(string) && b.type() == typeid(float)) {
        return a.convertible_to<string>() > to_string(b.convertible_to<float>()) ? a : ((a.convertible_to<string>() == to_string(b.convertible_to<float>())) ? boost::any("None") : boost::any(to_string(b.convertible_to<float>())));
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        return a.convertible_to<int>() > stoi(b.convertible_to<string>()) ? a : ((int)a.convertible_to<int>() == stoi(b.convertible_to<string>()) ? boost::any("None") : boost::any(stoi(b.convertible_to<string>())));