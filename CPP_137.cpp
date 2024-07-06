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
        std::string s1 = boost::any_cast<std::string>(a);
        std::string s2 = boost::any_cast<std::string>(b);
        if ((s1 == "None" || s2 == "None") && s1 != s2)
            return a > b ? a : b;
        else
            return (s1 == "None" || s2 == "None") ? "None" : (s1 > s2 ? a : b);
    }
    else if (a.type() == typeid(std::string)) {
        std::string s = boost::any_cast<std::string>(a);
        return (s == "None" || boost::any_cast<std::string>(b) == "None") ?
               "None" : (s > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") {
        return "None";
    }
    else {
        return (float)boost::any_cast<int>(a) > (float)boost::any_cast<int>(b) ? b : a;
    }
}