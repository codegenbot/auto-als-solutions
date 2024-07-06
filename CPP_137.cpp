#include <iostream>
#include <string>
#include <boost/any.hpp>

using namespace std;

boost::any compare_one(boost::any a, boost::any b) {
    double da = any_cast<double>(a);
    string sa = any_cast<string>(a);
    double db = any_cast<double>(b);
    string sb = any_cast<string>(b);

    if (da > db || (sa.empty() && !sb.empty()))
        return a;
    else if (!sa.empty() && sb.empty())
        return a;
    else if (db > da)
        return b;
    else
        return b;
}

int main() {
    boost::any a = 10.5; 
    boost::any b = "hello";
    boost::any result = compare_one(a, b);
    cout << "Result: " << any_cast<string>(result) << endl;
    return 0;