```
if (a.type() == typeid(int) && b.type() == typeid(float)) {
    if ((int)a Conversion::get<int>(a) >= (int) boost::any_cast<float>(b)) return a;
    else return b;
} else if (a.type() == typeid(float) && b.type() == typeid(int)) {
    if ((float)boost::any_cast<int>(a) >= (float)b) return a;
    else return b;
} else if (a.type() == typeid(string) && b.type() == typeid(int)) {
    int c = boost::any_cast<int>(b);
    if (((string)a).compare(0, string::npos, ".") == 0 || ((string)a).find(',') != string::npos) {
        if (((string)a).compare(0, ((string)a).size(), std::to_string(c)) >= 0) return a;
    } else {
        int x = boost::lexical_cast<int>(a.get_any());
        if (x >= c) return a;
    }
} else if (a.type() == typeid(int) && b.type() == typeid(string)) {
    int c = boost::any_cast<int>(a);
    if (((string)b).compare(0, string::npos, ".") == 0 || ((string)b).find(',') != string::npos) {
        if (((string)b).compare(0, ((string)b).size(), std::to_string(c)) >= 0) return b;
    } else {
        int x = boost::lexical_cast<int>(b.get_any());
        if (x >= c) return b;
    }
} else if (a.type() == typeid(string) && b.type() == typeid(string)) {
    if (((string)a).compare(0, ((string)a).size(), ((string)b).substr(((string)b).find('.') + 1, string::npos)) > 0) return a;
    else if (((string)a).compare(0, ((string)a).size(), ((string)b).substr(((string)b).find(',') + 1, string::npos)) > 0) return a;
    else if (((string)b).compare(0, ((string)b).size(), ((string)a).substr(((string)a).find('.') + 1, string::npos)) > 0) return b;
    else if (((string)b).compare(0, ((string)b).size(), ((string)a).substr(((string)a).find(',') + 1, string::npos)) > 0) return b;
} else {
    if (boost::any_cast<float>(a) > boost::any_cast<float>(b)) return a;
    else if (boost::any_cast<float>(b) > boost::any_cast<float>(a)) return b;
    else return boost::any("None");
}
return boost::any();