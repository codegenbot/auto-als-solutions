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

int miniRomanToNumber(int number) {
    std::string roman = "";
    for (int i = 0; i < sizeof(numerals)/sizeof(int); i++) {
        while (number >= numerals[i]) {
            if (romanNumerals[i] == "M") {
                roman += "M";
                number -= 1000;
            }
            else if (romanNumerals[i] == "CM") {
                roman += "CM";
                number -= 900;
            }
            else if (romanNumerals[i] == "D") {
                roman += "D";
                number -= 500;
            }
            else if (romanNumerals[i] == "CD") {
                roman += "CD";
                number -= 400;
            }
            else if (romanNumerals[i] == "C") {
                roman += "C";
                number -= 100;
            }
            else if (romanNumerals[i] == "XC") {
                roman += "XC";
                number -= 90;
            }
            else if (romanNumerals[i] == "L") {
                roman += "L";
                number -= 50;
            }
            else if (romanNumerals[i] == "XL") {
                roman += "XL";
                number -= 40;
            }
            else if (romanNumerals[i] == "X") {
                roman += "X";
                number -= 10;
            }
            else if (romanNumerals[i] == "IX") {
                roman += "IX";
                number -= 9;
            }
            else if (romanNumerals[i] == "V") {
                roman += "V";
                number -= 5;
            }
            else if (romanNumerals[i] == "IV") {
                roman += "IV";
                number -= 4;
            }
            else {
                roman += romanNumerals[i];
                number -= 1;
            }
        }
    }
    return roman;
}

int main() {
    assert(intToRoman(1000) == "M");
    std::cout << miniRomanToNumber(1999);
    return 0;
}