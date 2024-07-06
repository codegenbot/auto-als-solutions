#include <boost/any.hpp>
#include <iostream>
#include <string>

using namespace std;
using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<double>(a) > any_cast<double>(b)) {
        return a;
    } else if (any_cast<string>(a) > any_cast<string>(b)) {
        return a;
    } else if (any_cast<string>(b) > any_cast<string>(a)) {
        return b;
    } else {
        return "None";
    }
}