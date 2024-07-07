boost::any compare_one(boost::any a, boost::any b) {
    if (a.type() == typeid(int) && b.type() == typeid(float)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(double)) {
        return (int)b > (int)a ? b : a;
    }
    else if (a.type() == typeid(int) && b.type() == typeid(string)) {
        double val = stod(b.convert<string>().c_str());
        return val > (double)a ? b : a;
    }
    else if (a.type() == typeid(float) && b.type() == typeid(double)) {
        return (double)b > (float)a ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(double)) {
        double val = stod(b.convert<string>().c_str());
        return val > stod(a.convert<string>().c_str()) ? b : a;
    }
    else if (a.type() == typeid(string) && b.type() == typeid(string)) {
        double val1 = stod(a.convert<string>().c_str()), val2 = stod(b.convert<string>().c_str());
        return val2 > val1 ? b : a;
    }
    else {
        return boost::any("None");
    }
}