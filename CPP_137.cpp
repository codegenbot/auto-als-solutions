```cpp
#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (boost::any_cast<int>(b) > boost::any_cast<int>(a)) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (boost::any_cast<float>(b) > boost::any_cast<float>(a)) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str_a = boost::any_cast<string>(a);
        string str_b = boost::any_cast<string>(b);

        if ((str_a == "None" || str_b == "None") && str_a != str_b)
            return (str_a > str_b) ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        string str_a = boost::any_cast<string>(a);
        string str_b = boost::any_cast<string>(b);

        if ((str_a == "None" || str_b == "None") && str_a != str_b)
            return (str_a > str_b) ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(float)) {
        return (boost::any_cast<float>(b) > boost::any_cast<float>(a)) ? b : a;
    }
    else {
        return "None";
    }
}