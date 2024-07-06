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
        string strA = boost::any_cast<string>(a);
        string strB = boost::any_cast<string>(b);
        if ((strA == "None" || strB == "None") &&
            strA != strB)
            return strA > strB ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        string strA = boost::any_cast<string>(a);
        if (strA == "None" || boost::any_cast<string>(b) == "None")
            return "None";
        else
            return strA > boost::any_cast<string>(b) ? a : b;
    }
    else if (boost::any_cast<string>(a) == "None") {
        return "None";
    }
    else if (boost::any_cast<string>(b) == "None") {
        return a;
    }
    else {
        return boost::any_cast<string>(a) > boost::any_cast<string>(b) ? a : b;
    }
}