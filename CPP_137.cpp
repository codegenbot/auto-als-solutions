#include <boost/any.hpp>
#include <string>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return b;
    }
    if (a.type() == typeid(double) && b.type() == typeid(int)) {
        return b;
    }
    if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a);
        string s2 = boost::any_cast<string>(b);
        if (stod(s1) > stod(s2))
            return a;
        else if (stod(s1) < stod(s2))
            return b;
        else
            return boost::any("None");
    }
    if (a.type() == typeid(int) && b.type() == typeid(string)) {
        int i = boost::any_cast<int>(a);
        string s = boost::any_cast<string>(b);
        if (stod(s) > i)
            return b;
        else if (i > stod(s))
            return a;
        else
            return boost::any("None");
    }
    if (a.type() == typeid(string) && b.type() == typeid(int)) {
        string s = boost::any_cast<string>(a);
        int i = boost::any_cast<int>(b);
        if (stod(s) > i)
            return a;
        else if (i > stod(s))
            return b;
        else
            return boost::any("None");
    }
    return b;
}