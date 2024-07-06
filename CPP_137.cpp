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
        string s1 = boost::any_cast<string>(a);
        string s2 = boost::any_cast<string>(b);
        if ((s1 == "None" || s2 == "None") && s1 != s2)
            return s1 > s2 ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        string s = boost::any_cast<string>(a);
        if (s == "None")
            return "None";
        else
            return "None";
    }
    else if (boost::any_cast<string>(b) == "None")
        return "None";
    else if (a.type() == typeid(float)) {
        return boost::any_cast<float>(b) > (float)a ? b : a;
    }
    else if (b.type() == typeid(float)) {
        return boost::any_cast<float>(a) > (float)b ? a : b;
    }
    return "None";
}