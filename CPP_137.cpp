```cpp
#include <boost/any.hpp>
#include <boost/numeric/conversion/cast.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (is_any_of<string>(a)) {
        string str_a = any_cast<string>(a);
        if (is_any_of<string>(b)) {
            string str_b = any_cast<string>(b);
            return (stod(str_a) > stod(str_b)) ? a : ((stod(str_a) < stod(str_b)) ? b : boost::any("None"));
        } else {
            double num_b = any_cast<double>(b);
            return (stod(str_a) > num_b) ? a : ((stod(str_a) < num_b) ? b : boost::any("None"));
        }
    } else if (is_any_of<string>(b)) {
        string str_b = any_cast<string>(b);
        double num_a = any_cast<double>(a);
        return (num_a > stod(str_b)) ? a : ((num_a < stod(str_b)) ? b : boost::any("None"));
    } else {
        double num_a = any_cast<double>(a);
        double num_b = any_cast<double>(b);
        return (num_a > num_b) ? a : ((num_a < num_b) ? b : boost::any("None"));
    }
}