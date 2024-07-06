boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return boost::any_cast<float>(b) > boost::any_cast<int>(a)
            ? b
            : a;
    } else if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return boost::any_cast<double>(b) > boost::any_cast<int>(a)
            ? b
            : a;
    } else if (a.type() == typeid(float) && b.type() == typeid(double)) {
        return boost::any_cast<double>(b) > boost::any_cast<float>(a)
            ? b
            : a;
    } else if (a.type() == typeid(string) && b.type() == typeid(int)) {
        return boost::any_cast<string>(a) == "None"
            ? "None"
            : (boost::any_cast<int>(b) > 0.5 ? b : a);
    } else if (a.type() == typeid(string) && b.type() == typeid(double)) {
        return boost::any_cast<string>(a) == "None"
            ? "None"
            : (boost::any_cast<double>(b) > 0.5 ? b : a);
    } else if (a.type() == typeid(string) && b.type() == typeid(float)) {
        float f1 = boost::any_cast<float>(a);
        float f2 = boost::any_cast<float>(b);
        return f2 > f1 ? b : a;
    } else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        string s1 = boost::any_cast<string>(a);
        string s2 = boost::any_cast<string>(b);
        return s1.compare(s2) < 0 ? b : a;
    } else if (boost::any_cast<int>(a) > boost::any_cast<int>(b)) {
        return a;
    } else if (boost::any_cast<int>(a) == boost::any_cast<int>(b)) {
        return "None";
    } else {
        return b;
    }
}