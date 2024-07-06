#include <boost/any.hpp>
#include <string>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    int i1 = any_cast<int>(a);
    double d1 = any_cast<double>(a);
    std::string s1 = any_cast<std::string>(a);

    int i2 = any_cast<int>(b);
    double d2 = any_cast<double>(b);
    std::string s2 = any_cast<std::string>(b);

    if (i1 > i2) return a;
    else if (d1 > d2) return a;
    else if (s1 > s2) return a;
    else if (i1 == i2) return "None";
    else if (d1 == d2) return "None";
    else if (s1 == s2) return "None";
    return b;
}