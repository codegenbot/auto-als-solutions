#include <boost/any.hpp>
#include <boost/numeric/conversion/cast.hpp>
#include <string>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (is_any_of<std::string>(a)) {
        std::string str_a = any_cast<std::string>(a);
        if (is_any_of<std::string>(b)) {
            std::string str_b = any_cast<std::string>(b);
            return (std::stod(str_a) > std::stod(str_b)) ? a : ((std::stod(str_a) < std::stod(str_b)) ? b : boost::any("None"));
        } else {
            double num_b = any_cast<double>(b);
            return (std::stod(str_a) > num_b) ? a : ((std::stod(str_a) < num_b) ? b : boost::any("None"));
        }
    } else if (is_any_of<std::string>(b)) {
        std::string str_b = any_cast<std::string>(b);
        double num_a = any_cast<double>(a);
        return (num_a > std::stod(str_b)) ? a : ((num_a < std::stod(str_b)) ? b : boost::any("None"));
    } else {
        double num_a = any_cast<double>(a);
        double num_b = any_cast<double>(b);
        return (num_a > num_b) ? a : ((num_a < num_b) ? b : boost::any("None"));
    }
}