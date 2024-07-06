#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? boost::any(b) : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (float)a ? b : a;
    }
    else if (a.type() == typeid(std::string) && b.type() == typeid(std::string)) {
        std::string strA = boost::any_cast<std::string>(a);
        std::string strB = boost::any_cast<std::string>(b);
        
        if ((strA == "None" || strB == "None") && strA != strB)
            return a > b ? a : b;
        else
            return "None";
    }
    else if (a.type() == typeid(std::string)) {
        std::string str = boost::any_cast<std::string>(a);
        
        if ((str == "None" || boost::any_cast<std::string>(b) == "None"))
            return "None";
        else
            return str > boost::any_cast<std::string>(b) ? a : b;
    }
    else if (boost::any_cast<std::string>(a) == "None") {
        return "None";
    }
    
    return a;
}