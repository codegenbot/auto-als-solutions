#include <iostream>
#include <vector>
#include <string>

std::vector<std::string> romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
std::string intToRoman(int number) {
    std::string roman = "";
    for (int i = 0; i < sizeof(numerals)/sizeof(int); i++) {
        while (number >= numerals[i]) {
            roman += romanNumerals[i];
            number -= numerals[i];
        }
    }
    return roman;
}

int mainFunc() {
    assert(intToRoman(1000) == "M");
    std::cout << intToRoman(1999);
    return 0;
}