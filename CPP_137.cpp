#include <boost/any.hpp>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(std::string)) {
        std::string str = b.cast<std::string>().erase(0,1).erase(b.cast<std::string>()->length()-2,b.cast<std::string>()->length());
        return (std::stoi(str)) > a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > a ? b : a;
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        return a.cast<std::string>().compare(b.cast<std::string>()) > 0 ? a : boost::any(a);
    }
    else {
        return boost::any(a);
    }
}