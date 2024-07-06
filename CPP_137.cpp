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
    else return b;
}

int main() {
    boost::any a = 5;
    boost::any b = 10;
    boost::any result = compare_one(a, b);
    std::cout << "Result: " << any_cast<int>(result) << std::endl;
    return 0;
}