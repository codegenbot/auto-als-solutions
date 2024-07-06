#include <string>
#include <sstream>
#include <boost/any.hpp>
#include <boost/convert.hpp>

std::string convert(boost::any a) {
    if (a.type() == typeid(int)) {
        return std::to_string(boost::any_cast<int>(a));
    } else if (a.type() == typeid(double)) {
        return std::to_string(boost::any_cast<double>(a));
    } else if (a.type() == typeid(float)) {
        return std::to_string(boost::any_cast<float>(a));
    } else if (a.type() == typeid(std::string)) {
        return boost::any_cast<std::string>(a);
    }
}

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return b;
    } else if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return b;
    } else if (a.type() == typeid(float) && b.type() == typeid(double)) {
        return b;
    } else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        std::string str1 = convert(a);
        std::string str2 = convert(b);
        if (std::stod(str1) > std::stod(str2))
            return a;
        else if (std::stod(str1) < std::stod(str2))
            return b;
        else
            return boost::any("None");
    } else if ((a.type() == typeid(int) && b.type() == typeid(std::string)) ||
               (a.type() == typeid(float) && b.type() == typeid(std::string))) {
        std::string str = convert(a);
        double num2 = std::stod(convert(b));
        if (std::stod(str) > num2)
            return a;
        else if (std::stod(str) < num2)
            return b;
        else
            return boost::any("None");
    } else {
        return boost::any("None");
    }
}