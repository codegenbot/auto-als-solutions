#include <iostream>
#include <vector>
#include <string>
#include <cassert>

std::vector<std::string> romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
std::string int_to_mini_roman(int number) {
    std::string roman = "";
    for (int i = 0; i < sizeof(numerals)/sizeof(int); i++) {
        while (number >= numerals[i]) {
            roman += romanNumerals[i];
            number -= numerals[i];
        }
    }
    return roman;
}

int main() {
    assert(int_to_mini_roman(1000) == "M");
    return 0;
}