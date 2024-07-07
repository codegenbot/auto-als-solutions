#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return (int)boost::any_cast<int>(a) > (int)boost::any_cast<int>(b)
            ? b
            : (int)boost::any_cast<int>(a) > (int)boost::any_cast<int>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(float) && b.type() == typeid(float)) {
        return boost::any_cast<float>(a) > boost::any_cast<float>(b)
            ? b
            : boost::any_cast<float>(a) > boost::any_cast<float>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return boost::any_cast<string>(a) > boost::any_cast<string>(b)
            ? b
            : boost::any_cast<string>(a) > boost::any_cast<string>(b)
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(string)) {
        double val1 = stod(boost::any_cast<string>(a));
        if (b.type() == typeid(int)) {
            return val1 > (int)boost::any_cast<int>(b)
                ? b
                : val1 > (int)boost::any_cast<int>(b)
                    ? a
                    : boost::any("None");
        }
        else if (b.type() == typeid(float)) {
            return val1 > boost::any_cast<float>(b)
                ? b
                : val1 > boost::any_cast<float>(b)
                    ? a
                    : boost::any("None");
        }
    }
    else if (a.type() == typeid(int)) {
        double val2 = stod(boost::any_cast<string>(b));
        return int(val2) > (int)a
            ? b
            : int(val2) > (int)a
                ? a
                : boost::any("None");
    }
    else if (a.type() == typeid(float)) {
        double val1 = boost::any_cast<float>(a);
        double val2 = stod(boost::any_cast<string>(b));
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