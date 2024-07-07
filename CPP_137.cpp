#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(int)) {
        return ((int)b > (int)a) ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return ((float)b > (int)a) ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        string str = boost::any_cast<string>(b);
        if(str.length()>2&&str.substr(0,1)== "{" && str.substr(str.length()-2,2)==" "}{
            return ((stoi(str.erase(0,1).erase(str.length()-2,str.length()))) > (int)a) ? b : a;
        }
        else {
            return boost::any("None");
        }
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return ((float)b > (int)a) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return boost::any_cast<string>(a).compare(boost::any_cast<string>(b)) > 0 ? a : boost::any("None");
    }
    else {
        return boost::any("None");
    }
}

int main() {
    using namespace std;
    // use compare_one function here
}