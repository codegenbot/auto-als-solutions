```cpp
#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

std::string roman(int number) {
    std::string result = "";
    for (int i = 0; i < sizeof(numerals)/sizeof(int); i++) {
        while (number >= numerals[i]) {
            result += romanNumerals[i];
            number -= numerals[i];
        }
    }
    return result;
}

int main() {
    assert(roman(1000) == "M");
    std::cout << roman(2023);
    return 0;
}