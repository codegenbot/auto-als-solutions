```cpp
#include <boost/any.hpp>
#include <string>

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return boost::any((int)(b.convert_to<float>() > a.convert_to<int())) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return boost::any((float)(b.convert_to<int>()) > a.convert_to<float>()) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        std::string strA = boost::any_cast<std::string>(a);
        std::string strB = boost::any_cast<std::string>(b);
        
        if ((strA == "None" || strB == "None") && strA != strB)
            return a > b ? a : b;
        else
            return strA == "None" ? "None" : (strA > strB ? a : b);
    }
    else if (a.type() == typeid(string)) {
        std::string strA = boost::any_cast<std::string>(a);
        
        if ((strA == "None" || boost::any_cast<std::string>(b) == "None") && strA != boost::any_cast<std::string>(b))
            return a > b ? a : b;
        else
            return strA == "None" ? "None" : (strA > boost::any_cast<std::string>(b) ? a : b);
    }
    else if (boost::any_cast<std::string>(a) == "None") {
        std::string strA = boost::any_cast<std::string>(a);
        return strA;
    }
    else if (boost::any_cast<std::string>(b) == "None") {
        std::string strB = boost::any_cast<std::string>(b);
        return strB;
    }
    else
        return a > b ? a : b;
}