#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<double>(a) > any_cast<double>(b))
        return a;
    else if (any_cast<double>(b) > any_cast<double>(a))
        return b;

    if (any_cast<string>(a) > any_cast<string>(b))
        return a;
    else if (any_cast<string>(b) > any_cast<string>(a))
        return b;

    return "None";
}

int main() {
    boost::any a = 3.5; // input from user
    boost::any b = 2.8; // input from user

    boost::any result = compare_one(a, b);
    
    if (boost::any_cast<string>(result) == "None")
        cout << "The two numbers are equal.";
    else
        cout << "The bigger number is: " << boost::any_cast<string>(result);

    return 0;
}