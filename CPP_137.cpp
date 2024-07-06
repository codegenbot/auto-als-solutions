#include<string>
#include<boost/any.hpp>
using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return b;
    }
    else if (a.type() == typeid(double) && b.type() == typeid(int)) {
        return a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str_a = boost::any_cast<string>(a);
        string str_b = boost::any_cast<string>(b);
        if (str_a > str_b) {
            return a;
        }
        else if (str_a < str_b) {
            return b;
        }
        else {
            return boost::any("None");
        }
    }
    else if (a.type() == typeid(string) && b.type() == typeid(double)) {
        string str_a = boost::any_cast<string>(a);
        double num_b = boost::any_cast<double>(b);
        if (stod(str_a) > num_b) {
            return a;
        }
        else if (stod(str_a) < num_b) {
            return b;
        }
        else {
            return boost::any("None");
        }
    }
    else if (a.type() == typeid(double) && b.type() == typeid(string)) {
        double num_a = boost::any_cast<double>(a);
        string str_b = boost::any_cast<string>(b);
        if (num_a > stod(str_b)) {
            return a;
        }
        else if (num_a < stod(str_b)) {
            return b;
        }
        else {
            return boost::any("None");
        }
    }
    else {
        // This line should never be reached, but it's here for completeness
        return boost::any("None");
    }
}