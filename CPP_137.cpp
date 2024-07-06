```cpp
#include <boost/any.hpp>
#include <iostream>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<int>(a) > any_cast<int>(b)) return a;
    else if (any_cast<double>(a) > any_cast<double>(b)) return a;
    else if (any_cast<std::string>(a) > any_cast<std::string>(b)) return a;
    else if (any_cast<int>(a) == any_cast<int>(b)) return "None";
    else if (any_cast<double>(a) == any_cast<double>(b)) return "None";
    else if (any_cast<std::string>(a) == any_cast<std::string>(b)) return "None";
    return b;
}

int main() {
    boost::any a = 1; 
    boost::any b = 2; 

    std::cout << boost::any_cast<int>(compare_one(a, b)) << std::endl;

    a = 3.5; 
    b = 4.0; 

    std::cout << boost::any_cast<double>(compare_one(a, b)) << std::endl;

    a = "Hello"; 
    b = "World"; 

    std::cout << boost::any_cast<std::string>(compare_one(a, b)) << std::endl;
    return 0;
}