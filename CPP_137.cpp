#include <boost/any_cast.hpp>

boost::any compare_one(boost::any a, boost::any b) {
    if (!boost::any_cast<int>(&a)) {
        if (!boost::any_cast<int>(&b)) {
            if (std::to_string(std::stod(boost::any_cast<std::string>(a).c_str())) <
                std::to_string(std::stod(boost::any_cast<std::string>(b).c_str()))) {
                return b;
            } else if (std::to_string(std::stod(boost::any_cast<std::string>(a).c_str())) >
                        std::to_string(std::stod(boost::any_cast<std::string>(b).c_str()))) {
                return a;
            }
            return "None";
        } else if (a.convert_to<int>() > b.convert_to<int>()) {
            return a;
        } else if (a.convert_to<int>() < b.convert_to<int>()) {
            return b;
        }
        return "None";
    } else if (a.convert_to<int>() > b.convert_to<int>()) {
        return a;
    } else if (a.convert_to<int>() < b.convert_to<int>()) {
        return b;
    }
    return "None";
}