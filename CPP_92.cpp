```cpp
#include <iostream>

bool any_int(float a, float b, float c) {
    int ai = (int)a;
    int bi = (int)b;
    int ci = (int)c;

    return ((a == ai + bi + ci) || (b == ai + bi + ci) || (c == ai + bi + ci));
}

int main() {
    float a, b, c;
    std::cout << "Enter three floats: ";
    std::cin >> a >> b >> c;

    if(any_int(a, b, c))
        std::cout << "At least one of the numbers is an integer.\n";
    else
        std::cout << "None of the numbers are integers.\n";

    return 0;
}