#include <iostream>
#include <string>
#include <boost/any.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;
boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return max(a, b);
    } else if (a.type() == typeid(float) && b.type() == typeid(float)) {
        return max(a, b);
    } else if ((a.type() == typeid(string) || a.type() == typeid(double)) &&
               (b.type() == typeid(string) || b.type() == typeid(double))) {
        string strA = boost::any_cast<string>(a);
        string strB = boost::any_cast<string>(b);

        double numA = stod(strA);
        double numB = stod(strB);

        return (numA > numB) ? a : b;
    } else if ((a.type() == typeid(int) || a.type() == typeid(float)) &&
               (b.type() == typeid(string))) {
        double numA = boost::any_cast<double>(a);
        string strB = boost::any_cast<string>(b);

        return (numA > stod(strB)) ? a : b;
    } else if ((a.type() == typeid(string)) &&
               (b.type() == typeid(int) || b.type() == typeid(float))) {
        double numB = boost::any_cast<double>(b);
        string strA = boost::any_cast<string>(a);

        return (stod(strA) > numB) ? a : b;
    }

    if (boost::any_cast<int>(a) == boost::any_cast<int>(b)) {
        return boost::any("None");
    } else if (boost::any_cast<double>(a) > boost::any_cast<double>(b)) {
        return a;
    } else {
        return b;
    }
}

int main() {
    cout << boost::any_cast<string>(compare_one(1, 2.5)) << endl;
    cout << boost::any_cast<string>(compare_one(1, "2,3")) << endl;
    cout << boost::any_cast<string>(compare_one("5,1", "6")) << endl;
    cout << boost::any_cast<string>(compare_one("1", 1)) << endl;

    return 0;
}