#include <iostream>
#include <boost/any.hpp>

using namespace std;
using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (any_cast<int>(a) > any_cast<int>(b)) return a;
    else if (any_cast<double>(a) > any_cast<double>(b)) return a;
    else if (any_cast<string>(a) > any_cast<string>(b)) return a;
    else if (any_cast<int>(a) == any_cast<int>(b)) return "None";
    else if (any_cast<double>(a) == any_cast<double>(b)) return "None";
    else if (any_cast<string>(a) == any_cast<string>(b)) return "None";
    else return b;
}

int main() {
    boost::any a = 10; 
    boost::any b = 20; 

    boost::any result = compare_one(a, b);

    if (boost::any_cast<string>(result) == "None") {
        cout << "The numbers are equal." << endl;
    } else {
        cout << "The larger number is: " << boost::any_cast<int>(result) << endl;
    }

    return 0;
}