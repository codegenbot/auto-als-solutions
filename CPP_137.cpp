#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a.cast<int>() ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        string s = boost::any_cast<string>(b);
        return (stoi(s.erase(0,1).erase(s.length()-2,s.length()).c_str())) > (int)a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > (double)a ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a);
        string s2 = boost::any_cast<string>(b);
        return s1.compare(s2) > 0 ? a : boost::any("None");
    }
    else {
        return boost::any("None");
    }
}

int main() {
    using namespace std;
    boost::any a, b;
    cin >> a >> b;
    cout << compare_one(a, b);
}