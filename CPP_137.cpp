boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : (int)a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        return (stoi(b.cast<string>().erase(0,1).erase(b.length()-2,b.length()).c_str())) > a ?
            b : boost::any("None");
    }
    else if (a.type() == typeid(float) && b.type() == typeid(int)) {
        return (float)b > a ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        return a.cast<string>().compare(b.cast<string>()) > 0 ? a : (boost::any("None"));
    }
    else {
        return boost::any("None");
    }
}