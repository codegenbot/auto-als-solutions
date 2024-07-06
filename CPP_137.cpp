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

        if ((str1 == "None" || str2 == "None") && str1 != str2)
            return a > b ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(std::string)) {
        std::string str = boost::any_cast<std::string>(a);

        return (str == "None" || boost::any_cast<std::string>(b) == "None") ?
               "None" : (str > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (boost::any_cast<std::string>(a) == "None" || boost::any_cast<std::string>(b) == "None") {
        return "None";
    }
    else if (boost::any_cast<float>(b) > boost::any_cast<float>(a)) {
        return b;
    }