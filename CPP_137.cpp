#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)boost::any_cast<float>(b) > (int)boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a);
        string s2 = boost::any_cast<string>(b);
        return s1 > s2 ? a : b;
    }
    else if ((a.type() == typeid(int) || a.type() == typeid(float)) && (b.type() == typeid(string))) {
        return "None";
    }
    else if ((a.type() == typeid(string)) && (b.type() == typeid(int) || b.type() == typeid(float))) {
        return "None";
    }
    else {
        return "None";
    }
}