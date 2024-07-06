#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    double val1 = any_cast<double>(a);
    double val2 = any_cast<double>(b);

    if (val1 > val2)
        return a;
    else if (!boost::any_empty(b) && any_cast<string>(a) > any_cast<string>(b))
        return a;
    else if (!boost::any_empty(a) && any_cast<string>(b) > any_cast<string>(a))
        return b;
    else
        return boost::any("None");
}