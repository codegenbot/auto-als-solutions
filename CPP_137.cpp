```cpp
#include <boost/any.hpp>
#include <boost/config.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<int>(a) > any_cast<int>(b)) return a;
    else if (any_cast<double>(a) > any_cast<double>(b)) return a;
    else if (any_cast<std::string>(a) > any_cast<std::string>(b)) return a;
    else if (any_cast<int>(a) == any_cast<int>(b)) return boost::any("None");
    else if (any_cast<double>(a) == any_cast<double>(b)) return boost::any(0.0);
    else if (any_cast<std::string>(a) == any_cast<std::string>(b)) return boost::any("None");
    return b;
}