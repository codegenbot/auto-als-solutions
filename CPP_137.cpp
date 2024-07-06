#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<double>(a) > any_cast<double>(b))
        return a;
    else if (!boost::any_empty(any_cast<boost::any>(b)) && any_cast<string>(a) > any_cast<string>(b))
        return a;
    else if (!boost::any_empty(any_cast<boost::any>(a)) && any_cast<string>(b) > any_cast<string>(a))
        return b;
    else
        return boost::any("None");
}