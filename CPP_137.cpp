#include <iostream>
#include <string>
#include <boost/any.hpp>
#include <boost/convert.hpp>

using namespace std;
using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    any_cast<double>(a) > any_cast<double>(b)
        ? return a
        : any_cast<string>(a) > any_cast<string>(b)
            ? return a
            : any_cast<string>(b) > any_cast<string>(a)
                ? return b
                : return "None";
}