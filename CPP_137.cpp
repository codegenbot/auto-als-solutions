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
        if ((boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") &&
            boost::any_cast<std::string>(a) != boost::any_cast<std::string>(b))
            return a > b ? a : b;
        else
            return boost::any_cast<std::string>(a);
    }
    else if (a.type() == typeid(std::string)) {
        if ((boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") &&
            boost::any_cast<std::string>(a) != boost::any_cast<std::string>(b))
            return a > b ? a : b;
        else
            return boost::any_cast<std::string>(a);
    }
    else if (b.type() == typeid(std::string)) {
        if ((boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") &&
            boost::any_cast<std::string>(a) != boost::any_cast<std::string>(b))
            return a > b ? a : b;
        else
            return boost::any_cast<std::string>(a);
    }
    else if (a.type() == typeid(float)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<int>(a) ? b : a;
    }
    else if (b.type() == typeid(float)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<int>(a) ? b : a;
    }
    return "None";
}