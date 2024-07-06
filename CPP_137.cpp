#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

class Any {
public:
    enum Type { INT, FLOAT, DOUBLE, STRING };

    template<typename T>
    void insert(T value) {
        if (value instanceof int) {
            data.push_back(to_string(value));
        }
        else if (value instanceof float || value instanceof double) {
            data.push_back(to_string(value));
        }
        else if (value instanceof string) {
            data.push_back(string(value));
        }
    }

    Type get_type() const {
        return type;
    }

    vector<string> convert() const {
        return data;
    }

private:
    vector<string> data;
    Type type;
};

Any compare_one(Any a, Any b) {
    if (a.get_type() == Any::INT && b.get_type() == Any::FLOAT) {
        return b;
    }
    else if (a.get_type() == Any::INT && b.get_type() == Any::DOUBLE) {
        return b;
    }
    else if (a.get_type() == Any::FLOAT && b.get_type() == Any::DOUBLE) {
        return b;
    }
    else if (a.get_type() == Any::STRING && b.get_type() == Any::STRING) {
        vector<string> v1 = a.convert();
        vector<string> v2 = b.convert();
        double num1, num2;
        for (const auto& s : v1) {
            num1 = stod(s);
        }
        for (const auto& s : v2) {
            num2 = stod(s);
        }
        if (num1 > num2)
            return a;
        else if (num1 < num2)
            return b;
        else
            return Any();
    }
    else if ((a.get_type() == Any::INT && b.get_type() == Any::STRING) ||
             (a.get_type() == Any::FLOAT && b.get_type() == Any::STRING)) {
        vector<string> v = a.convert();
        double num2;
        for (const auto& s : v) {
            num2 = stod(s);
        }
        string str = b.convert()[0];
        if (stod(str) > num2)
            return a;
        else if (stod(str) < num2)
            return b;
        else
            return Any();
    }
    else {
        return Any();
    }
}