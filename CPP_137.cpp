```cpp
#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)boost::any_cast<float>(b) > (int)a ? boost::any(b) : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string strA = boost::any_cast<string>(a);
        string strB = boost::any_cast<string>(b);
        if ((strA == "None" || strB == "None") && strA != strB)
            return a > b ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        string strA = boost::any_cast<string>(a);
        string strB = boost::any_cast<string>(b);
        return (strA == "None" || strB == "None") ? "None" : (strA > strB ? a : b);
    }
    else if (b.type() == typeid(string)) {
        string strA = boost::any_cast<string>(a);
        string strB = boost::any_cast<string>(b);
        return (strA == "None" || strB == "None") ? "None" : (strA > strB ? a : b);
    }
    else if (a.type() == typeid(float)) {
        return boost::any_cast<float>(b) > (float)a ? b : a;
    }
    else if (b.type() == typeid(float)) {
        return boost::any_cast<float>(b) > (float)a ? b : a;
    }
    return "None";
}