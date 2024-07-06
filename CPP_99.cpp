#include <string>

int closest_integer(std::string value) {
    double num = stod(value);
    int integerPart = (int)num;
    if (fabs(num - integerPart) >= 0.5) {
        return round(num);
    } else {
        if (num > 0)
            return integerPart + 1;
        else
            return integerPart - 1;
    }
}