#include <string>
#include <algorithm>
#include <boost/any.hpp>
#include <boost/lexical_cast.hpp>

using namespace std;
using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (is_any_of<a>(double())) {
        if (is_any_of<b>(double())) {
            double da = boost::any_cast<double>(a);
            double db = boost::any_cast<double>(b);
            return da > db ? a : (da == db ? "None" : b);
        } else {
            string sa = boost::any_cast<string>(a);
            double db = boost::any_cast<double>(b);
            if (db > stod(sa))
                return a;
            else
                return b;
        }
    } else {
        string sa = boost::any_cast<string>(a);
        string sb = boost::any_cast<string>(b);
        return stod(sb) > stod(sa) ? b : (stod(sa) == stod(sb) ? "None" : a);
    }
}