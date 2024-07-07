#include <vector>
#include <string>

std::vector<std::string> romanNumbers = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
std::vector<int> decimalValues = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

std::string int_to_mini_roman(int number) {
    std::string roman = "";
    for (int i = 0; i < decimalValues.size(); i++) {
        while (number >= decimalValues[i]) {
            number -= decimalValues[i];
            roman += romanNumbers[i];
        }
    }
    return roman;
}