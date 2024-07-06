#include <boost/any.hpp>
#include <iostream>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    int intA = any_cast<int>(a);
    int intB = any_cast<int>(b);
    
    double doubA = any_cast<double>(a);
    double doubB = any_cast<double>(b);
    
    std::string strA = any_cast<std::string>(a);
    std::string strB = any_cast<std::string>(b);

    if (intA > intB) return a;
    else if (doubA > doubB) return a;
    else if (strA > strB) return a;
    else if (intA == intB && doubA == doubB && strA == strB) return "None";
    else return b;
}

int main() {
    boost::any a = 10;
    boost::any b = 5;
    std::cout << any_cast<int>(compare_one(a, b)) << "\n";
    
    a = 10.2;
    b = 5.5;
    std::cout << any_cast<double>(compare_one(a, b)) << "\n";
    
    a = "hello";
    b = "hi";
    std::cout << *any_cast<std::string*>(&compare_one(a, b)) << "\n";
    
    return 0;
}