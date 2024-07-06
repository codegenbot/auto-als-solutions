#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (boost::any_cast<double>(a) > boost::any_cast<double>(b))
        return a;
    else if (boost::any_cast<double>(b) > boost::any_cast<double>(a))
        return b;

    if (boost::any_cast<string>(a) > boost::any_cast<string>(b))
        return a;
    else if (boost::any_cast<string>(b) > boost::any_cast<string>(a))
        return b;

    return boost::any("None");
}