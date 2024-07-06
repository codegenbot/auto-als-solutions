#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<double>(a) > any_cast<double>(b))
        return a;
    else if (any_cast<string>(a).compare(any_cast<string>(b)) > 0)
        return a;
    else if (any_cast<string>(b).compare(any_cast<string>(a)) > 0)
        return b;
    else
        return boost::any("None");
}