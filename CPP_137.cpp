boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : "None";
    } else if (a.type() == typeid(float) && b.type() == typeid(string)) {
        return (float)boost::any_cast<string>(b) > a ? b : "None";
    } else if (a.type() == typeid(string) && b.type() == typeid(int)) {
        return boost::any_cast<string>(a) > to_string((int)b) ? a : "None";
    } else if (a.type() == typeid(string) && b.type() == typeid(float)) {
        return boost::any_cast<string>(a) > to_string((float)b) ? a : "None";
    } else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        return (int)a > stoi(boost::any_cast<string>(b)) ? a : "None";
    } else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)a > (int)b ? a : "None";
    }
    return b;
}