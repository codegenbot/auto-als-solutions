#include <boost/convert.hpp>
#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return any_cast<int>(a) > any_cast<int>(b)
            ? b
            : any_cast<int>(a) > any_cast<int>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(float) && b.type() == typeid(float)) {
        return any_cast<float>(a) > any_cast<float>(b)
            ? b
            : any_cast<float>(a) > any_cast<float>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return any_cast<string>(a) > any_cast<string>(b)
            ? b
            : any_cast<string>(a) > any_cast<string>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(string)) {
        double val1 = stod(any_cast<string>(a));
        if (b.type() == typeid(int)) {
            return val1 > any_cast<int>(b)
                ? b
                : val1 > any_cast<int>(b)
                    ? a
                    : boost::any("None");
        }
        else if (b.type() == typeid(float)) {
            return val1 > any_cast<float>(b)
                ? b
                : val1 > any_cast<float>(b)
                    ? a
                    : boost::any("None");
        }
    }
    else if (a.type() == typeid(int)) {
        double val2 = stod(any_cast<string>(b));
        return val2 > a
            ? b
            : val2 > a
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(float)) {
        double val1 = any_cast<float>(a);
        double val2 = stod(any_cast<string>(b));
        return val1 > val2
            ? b
            : val1 > val2
                ? a
                : boost::any("None");
    }
    else {
        return boost::any("None");
    }
}