std::string miniRom(int number) {
    std::string result = "";
    std::string romanNumerals[13];
    int numerals[] = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    for (int i = 0; i < 13; i++) {
        romanNumerals[i] = (numerals[i] == 1000) ? "M" :
            ((numerals[i] == 900) ? "CM" : 
             ((numerals[i] == 500) ? "D" : 
             ((numerals[i] == 400) ? "CD" : 
             ((numerals[i] == 100) ? "C" : 
             ((numerals[i] == 90) ? "XC" : 
             ((numerals[i] == 50) ? "L" : 
             ((numerals[i] == 40) ? "XL" : 
             ((numerals[i] == 10) ? "X" : 
             ((numerals[i] == 9) ? "IX" : 
             ((numerals[i] == 5) ? "V" : 
             ((numerals[i] == 4) ? "IV" : "I")))))))));
    }
    std::vector<std::string> romanNumeralsVector(romanNumerals, romanNumerals + 13);
    const int arraySize = sizeof(numerals) / sizeof(numerals[0]);
    for (int i = 0; i < arraySize; i++) {
        while (number >= numerals[i]) {
            result += romanNumeralsVector[i];
            number -= numerals[i];
        }
    }
    return result;
}

int main() {
    std::cout << miniRom(2023);
    return 0;
}