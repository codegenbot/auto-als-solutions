#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)boost::any_cast<float>(b) > (int)boost::any_cast<int>(a) ? boost::any(b) : boost::any(a);
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<float>(a) ? boost::any(b) : boost::any(a);
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        if ((boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") &&
            boost::any_cast<std::string>(a) != boost::any_cast<std::string>(b))
            return (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b) ? a : b);
        else
            return boost::any("None");
    }
    else if (a.type() == typeid(std::string)) {
        return (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (boost::any_cast<std::string>(b).type() == typeid(std::string)) {
        return (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") ?
               boost::any("None") : (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (a.type() == typeid(float)) {
        return boost::any((float)boost::any_cast<float>(b) > (float)boost::any_cast<float>(a) ? b : a);
    }
    else if (b.type() == typeid(float)) {
        return boost::any((float)boost::any_cast<float>(b) > (float)boost::any_cast<float>(a) ? b : a);
    }
    return boost::any("None");
}