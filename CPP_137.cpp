#include <boost/any.hpp>
#include <boost/convert.hpp>
#include <string>
#include <iostream>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return boost::any((int)b > (int)a ? b : a);
    }
    else if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return boost::any((int)b > (int)a ? b : a);
    }
    else if (a.type() == typeid(int) && b.type() == typeid(std::string)) {
        double val = std::stod(b.convert<std::string>().c_str());
        return val > (double)a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(double)) {
        return boost::any((double)b > (float)a ? b : a);
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(double)) {
        double val = std::stod(b.convert<std::string>().c_str());
        return val > std::stod(a.convert<std::string>().c_str()) ? b : a;
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        double val1 = std::stod(a.convert<std::string>().c_str()), val2 = std::stod(b.convert<std::string>().c_str());
        return val2 > val1 ? b : a;
    }
    else {
        return boost::any("None");
    }
}