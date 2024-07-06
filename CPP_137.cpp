#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str1 = boost::any_cast<string>(a), str2 = boost::any_cast<string>(b);
        return str1 > str2 ? a : b;
    }
    else if ((a.type() == typeid(string) && b.type() != typeid(string)) || (a.type() != typeid(string) && b.type() == typeid(string))) {
        return "None";
    }
    else if (a.type() == typeid(float) && b.type() == typeid(float)) {
        return boost::any_cast<float>(b) > boost::any_cast<float>(a) ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return boost::any_cast<int>(b) > boost::any_cast<int>(a) ? b : a;
    }
    return "None";
}