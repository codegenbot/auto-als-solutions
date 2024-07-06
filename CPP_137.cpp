#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<int>(a) > any_cast<int>(b)) return a;
    else if (any_cast<double>(a) > any_cast<double>(b)) return a;
    else if (any_cast<string>(a) > any_cast<string>(b)) return a;
    else if (any_cast<int>(a) == any_cast<int>(b)) return "None";
    else if (any_cast<double>(a) == any_cast<double>(b)) return "None";
    else if (any_cast<string>(a) == any_cast<string>(b)) return "None";
    else return b;
}