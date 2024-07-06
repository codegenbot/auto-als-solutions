#include <boost/any.hpp>
using namespace std;
using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    double da = any_cast<double>(a);
    string sa = any_cast<string>(a);
    double db = any_cast<double>(b);
    string sb = any_cast<string>(b);

    if (da > db || (!db.has_value() && !sa.empty()))
        return a;
    else if (sb > sa || (!da.has_value() && !sb.empty()))
        return b;
    else
        return boost::any("None");
}