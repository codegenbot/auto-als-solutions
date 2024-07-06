#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return boost::any(b.convert_to<int>() > boost::any_cast<int>(a) ? b : a);
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return boost::any(boost::any_cast<float>(b) > boost::any_cast<float>(a) ? b : a);
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a), s2 = boost::any_cast<string>(b);
        return boost::any((s1 == "None" || s2 == "None") ? ((s1 > s2) ? a : b) : (s1 > s2 ? b : a));
    }
    else if (a.type() == typeid(string)) {
        string s = boost::any_cast<string>(a);
        return boost::any((s == "None" || boost::any_cast<string>(b) == "None") ? ((s > boost::any_cast<string>(b)) ? a : b) : (s > boost::any_cast<string>(b) ? b : a));
    }
    else if (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") {
        return boost::any((boost::any_cast<string>(a) > boost::any_cast<string>(b)) ? a : b);
    }
    return boost::any("None");
}