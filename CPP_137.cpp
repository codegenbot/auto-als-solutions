#include <string>
#include <boost/any.hpp>

boost::any compare_one(boost::any a, boost::any b) {
    bool is_number_a = false;
    bool is_number_b = false;

    if (a.type() == typeid(int)) {
        is_number_a = true;
    } else if (a.type() == typeid(float) || a.type() == typeid(double) || a.type() == typeid(long double)) {
        is_number_a = true;
    } else {
        try {
            boost::any_cast<double>(a);
            is_number_a = true;
        } catch (...) {
            // a is not a number
        }
    }

    if (b.type() == typeid(int)) {
        is_number_b = true;
    } else if (b.type() == typeid(float) || b.type() == typeid(double) || b.type() == typeid(long double)) {
        is_number_b = true;
    } else {
        try {
            boost::any_cast<double>(b);
            is_number_b = true;
        } catch (...) {
            // b is not a number
        }
    }

    if (is_number_a && is_number_b) {
        if (boost::any_cast<double>(a) > boost::any_cast<double>(b)) {
            return a;
        } else if (boost::any_cast<double>(a) < boost::any_cast<double>(b)) {
            return b;
        } else {
            return boost::any("None");
        }
    }

    // one of them is not a number, compare the other
    if (!is_number_a && !is_number_b) {
        if (boost::any_cast<std::string>(a) > boost::any_cast<std::string>(b)) {
            return a;
        } else if (boost::any_cast<std::string>(a) < boost::any_cast<std::string>(b)) {
            return b;
        } else {
            return boost::any("None");
        }
    }

    // one of them is a number, the other is not
    if (!is_number_a && is_number_b) {
        return b;
    } else if (is_number_a && !is_number_b) {
        return a;
    }

    return boost::any("None");
}