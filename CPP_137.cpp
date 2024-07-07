Here's the completed code:

```cpp
#include <boost/any.hpp>
#include <string>
#include <algorithm>

using namespace boost;

boost::any compare_one(boost::any a, boost::any b) {
    if (is_any_of<a>(std::string("int")) && is_any_of<b>(std::string("float")) || is_any_of<a>(std::string("float")) && is_any_of<b>(std::string("int"))) {
        float fa = boost::any_cast<float>(a);
        float fb = boost::any_cast<float>(b);
        if (fa > fb)
            return a;
        else if (fb > fa)
            return b;
        else
            return boost::any("None");
    }
    else if ((is_any_of<a>(std::string("int")) && is_any_of<b>(std::string("int"))) || (is_any_of<a>(std::string("float")) && is_any_of<b>(std::string("float")))) {
        int ia = boost::any_cast<int>(a);
        int ib = boost::any_cast<int>(b);
        if (ia > ib)
            return a;
        else if (ib > ia)
            return b;
        else
            return boost::any("None");
    }
    else if ((is_any_of<a>(std::string("int")) && is_any_of<b>(std::string("float"))) || (is_any_of<a>(std::string("float")) && is_any_of<b>(std::string("int")))) {
        int ia = boost::any_cast<int>(a);
        float fb = boost::any_cast<float>(b);
        if (ia > fb)
            return a;
        else if (fb > ia)
            return b;
        else
            return boost::any("None");
    }
    else if ((is_any_of<a>(std::string("float")) && is_any_of<b>(std::string("string"))) || (is_any_of<a>(std::string("string")) && is_any_of<b>(std::string("float")))) {
        float fa = boost::any_cast<float>(a);
        std::string sb = boost::any_cast<std::string>(b);
        if (fa > atof(sb.c_str()))
            return a;
        else if (atof(sb.c_str()) > fa)
            return b;
        else
            return boost::any("None");
    }
    else {
        std::string sa = boost::any_cast<std::string>(a);
        std::string sb = boost::any_cast<std::string>(b);
        if (sa.compare(sb) > 0)
            return a;
        else if (sb.compare(sa) > 0)
            return b;
        else
            return boost::any("None");
    }
}