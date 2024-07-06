```cpp
#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? b : a;
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        std::string str1 = boost::any_cast<std::string>(a);
        std::string str2 = boost::any_cast<std::string>(b);
        if (str1 == "None" || str2 == "None") return a > b ? a : b;
        else return str1 > str2 ? a : b;
    }
    else if (a.type() == typeid(std::string)) {
        std::string str = boost::any_cast<std::string>(a);
        return str == "None" || b.type() != typeid(std::string) ?
               "None" : (str > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (b.type() == typeid(std::string)) {
        std::string str = boost::any_cast<std::string>(b);
        return boost::any_cast<std::string>(a) == "None" || str == "None" ?
               "None" : (boost::any_cast<std::string>(a) > str ? a : b);
    }
    else if (a.type() == typeid(float)) {
        return (float)b > (float)a ? b : a;
    }
    else if (b.type() == typeid(float)) {
        return (float)b > (float)a ? b : a;
    }
    return "None";
}