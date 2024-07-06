#include <vector>
#include <string>

vector<string> romanNumerals = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
string int_to_mini_roman(int number) {
    string roman = "";
    for (int i = 0; i < sizeof(numerals)/sizeof(int); i++) {
        while (number >= numerals[i]) {
            roman += romanNumerals[i];
            number -= numerals[i];
        }
    }
    return roman;
}

assert (int_to_mini_roman(1000) == "M");