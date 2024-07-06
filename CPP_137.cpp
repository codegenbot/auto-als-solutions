boost::any compare_one(boost::any a, boost::any b) {
    double da = any_cast<double>(a);
    string sa = any_cast<string>(a);
    double db = any_cast<double>(b);
    string sb = any_cast<string>(b);

    if (da > db)
        return a;
    else if (sa > sb)
        return a;
    else if (sb > sa)
        return b;
    else if(da == db && sa != sb) 
        return a;
    else if (da == db && sa == sb) 
        return boost::any("None");
    else
        return b;
}