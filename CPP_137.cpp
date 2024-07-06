#include <iostream>
#include <string>

std::string compareOne(double a, std::string b) {
    if (a > 0 || (!b.empty()))
        return "Greater";
    else if (!b.empty())
        return "Equal";
    else
        return "Less";
}

int main() {
    double a = 10.5; 
    std::string b = "hello";
    std::string result = compareOne(a, b);
    std::cout << "Result: " << result << std::endl;
    return 0;
}