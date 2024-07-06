#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? boost::any(std::to_string(b.convert_to<float>())) : boost::any(std::to_string(a.convert_to<int>()));
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? boost::any(std::to_string(b.convert_to<float>())) : boost::any(std::to_string(a.convert_to<int>()));
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a), s2 = boost::any_cast<string>(b);
        return (s1 == "None" || s2 == "None") ? a : ((s1 > s2) ? a : b);
    }
    else if (a.type() == typeid(string)) {
        string s = boost::any_cast<string>(a);
        return (s == "None" || boost::any_cast<string>(b) == "None") ? ("None") : ((s > boost::any_cast<string>(b)) ? a : b);
    }
    else if (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") {
        return ("None");
    }
    else {
        return (boost::any_cast<string>(a) > boost::any_cast<string>(b)) ? a : b;
    }
}