#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)boost::any_cast<int>(a) ? boost::any(b) : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)boost::any_cast<int>(b) > (float)boost::any_cast<int>(a) ? boost::any(b) : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str1 = boost::any_cast<string>(a);
        string str2 = boost::any_cast<string>(b);

        if ((str1 == "None" || str2 == "None") && str1 != str2)
            return str1 > str2 ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(string)) {
        string s = boost::any_cast<string>(a);
        if (s == "None" || boost::any_cast<string>(b) == "None") 
            return "None";
        else if (s > boost::any_cast<string>(b))
            return a;
        else
            return b;
    }
    else if (boost::any_cast<string>(a) == "None" || boost::any_cast<string>(b) == "None") 
        return "None";
    else if (boost::any_cast<string>(a) > boost::any_cast<string>(b))
        return a;
    else
        return b;
}