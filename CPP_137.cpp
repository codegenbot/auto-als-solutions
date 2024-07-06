#include <boost/any.hpp>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return b;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return b;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(double)) {
        return b;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str1 = a.convert<string>();
        string str2 = b.convert<string>();
        if (stod(str1) > stod(str2))
            return a;
        else if (stod(str1) < stod(str2))
            return b;
        else
            return boost::any("None");
    }
    else if ((a.type() == typeid(int) && b.type() == typeid(string)) ||
             (a.type() == typeid(float) && b.type() == typeid(string))) {
        string str = a.convert<string>();
        double num2 = stod(b.convert<string>());
        if (stod(str) > num2)
            return a;
        else if (stod(str) < num2)
            return b;
        else
            return boost::any("None");
    }
    else {
        return boost::any("None");
    }
}