```cpp
#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? boost::any(b) : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? boost::any(b) : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        if ((boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") &&
            boost::any_cast<string>(a) != boost::any_cast<string>(b))
            return a > b ? a : b;
        else
            return boost::any("None");
    }
    else if (a.type() == typeid(string)) {
        return (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<string>(a) > boost::any_cast<string>(b) ? a : b);
    }
    else if (b.type() == typeid(string)) {
        return (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<string>(a) > boost::any_cast<string>(b) ? a : b);
    }
    else if (a.type() == typeid(float)) {
        return (float)b > (float)a ? boost::any(b) : a;
    }
    else if (b.type() == typeid(float)) {
        return (float)b > (float)a ? boost::any(b) : a;
    }
    return boost::any("None");
}