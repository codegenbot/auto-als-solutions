```cpp
#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    double va = any_cast<double>(a);
    double vb = any_cast<double>(b);

    if (va > vb)
        return a;
    else if (vb > va)
        return b;

    string sa = any_cast<string>(a);
    string sb = any_cast<string>(b);

    if (sa > sb)
        return a;
    else if (sb > sa)
        return b;

    return boost::any("None");
}