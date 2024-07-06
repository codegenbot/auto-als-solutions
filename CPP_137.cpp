using boost::any_cast;

boost::any compare_one(boost::any a, boost::any b) {
    float fa = any_cast<float>(a);
    float fb = any_cast<float>(b);

    if (fa > fb) return a;
    else if (fb > fa) return b;

    bool sa = any_cast<bool>(a);
    bool sb = any_cast<bool>(b);

    if (sa > sb) return a;
    else if (sb > sa) return b;

    std::string s1 = any_cast<std::string>(a);
    std::string s2 = any_cast<std::string>(b);

    if (s1.compare(s2) > 0) return a;
    else if (s2.compare(s1) > 0) return b;

    return "None";
}