#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        string str = boost::any_cast<string>(b);
        string temp = str.erase(0,1).erase(str.length()-2,str.length());
        int num = stoi(temp);
        return num > boost::any_cast<int>(a) ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return boost::any_cast<float>(b) > boost::any_cast<float>(a) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string str1 = boost::any_cast<string>(a);
        string str2 = boost::any_cast<string>(b);
        return str1.compare(str2) > 0 ? a : boost::any("None");
    }
    else {
        return boost::any("None");
    }
}

int main() {
    using namespace std;
    cout << compare_one(5, 3.14) << endl;
    cout << compare_one(10, "123") << endl;
    cout << compare_one(1.2f, 7) << endl;
    cout << compare_one("hello", "world") << endl;
}