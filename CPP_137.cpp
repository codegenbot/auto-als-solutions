#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? boost::any(b) : boost::any(a);
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? boost::any(b) : boost::any(a);
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        if ((boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") &&
            boost::any_cast<std::string>(a) != boost::any_cast<std::string>(b))
            return a > b ? boost::any(a) : boost::any(b);
        else
            return boost::any("None");
    }
    else if (a.type() == typeid(std::string)) {
        return (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b) ? boost::any(a) : boost::any(b));
    }
    else if (boost::any_cast<std::string>(b).type() == typeid(std::string)) {
        return (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b) ? boost::any(a) : boost::any(b));
    }
    else if (a.type() == typeid(float)) {
        return (float)b > (float)a ? boost::any(b) : boost::any(a);
    }
    else if (b.type() == typeid(float)) {
        return (float)b > (float)a ? boost::any(b) : boost::any(a);
    }
    return boost::any("None");
}