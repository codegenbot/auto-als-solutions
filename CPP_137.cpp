#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)boost::any_cast<float>(b) > (int)a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        if ((boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") &&
            boost::any_cast<string>(a) != boost::any_cast<string>(b))
            return a > b ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        return boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None" ?
               "None" : (boost::any_cast<string>(a) > boost::any_cast<string>(b) ? a : b);
    }
    else if (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") {
        return "None";
    }
    else {
        return (float)boost::any_cast<int>(a) > (float)boost::any_cast<int>(b) ? a : b;
    }
}