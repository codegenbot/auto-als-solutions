#include <iostream>
#include <vector>
#include <string>
#include <cassert>

std::vector<std::string> romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
std::string int_to_mini_rom(int number) {
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
    assert(int_to_mini_rom(1000) == "M");
    std::cout << int_to_mini_rom(2023);
    return 0;
}