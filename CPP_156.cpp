#include <iostream>
#include <vector>
#include <string>

std::string romanNumerals[13];
int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

std::string miniRom(int number) {
    std::string result = "";
    const int arraySize = sizeof(numerals) / sizeof(numerals[0]);
    for (int i = 0; i < arraySize; i++) {
        while (number >= numerals[i]) {
            result += romanNumerals[i];
            number -= numerals[i];
        }
    }
    return result;
}

int main() {
    std::cout << miniRom(2023);
    return 0;
}