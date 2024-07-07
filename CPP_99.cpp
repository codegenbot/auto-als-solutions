#include <string>

int closest_integer(std::string value) {
    double num = stod(value);
    int integerPart = (int)num;
    if (abs(num - integerPart) >= 0.5) {
        return num > integerPart ? integerPart + 1 : integerPart - 1;
    } else {
        return integerPart;
    }
}