```cpp
#include <cmath>
#include <iostream>

bool is_simple_power(int x, int n) {
    double log_value = log((double)x) / log((double)n);
    return round(log_value) == log_value;
}

int main() {
    int x, n;
    std::cout << "Enter the value of x: ";
    std::cin >> x;
    std::cout << "Enter the value of n: ";
    std::cin >> n;
    if (is_simple_power(x, n))
        std::cout << x << " is a simple power of " << n << ".\n";
    else
        std::cout << x << " is not a simple power of " << n << ".\n";
    return 0;
}